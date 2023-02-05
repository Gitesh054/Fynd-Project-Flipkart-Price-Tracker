from flask import Blueprint, render_template, request, flash
from models import pricetracker
from tracker import track
from main import db

view = Blueprint('views', __name__)


@view.route("/")
def home():
    return render_template("show.html",products=pricetracker.query.all())


@view.route("/show.html", methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        'add entry to DB'
        url = request.form.get('url')
        try:
            items = track(url)
        except:
            return render_template("show.html",products=pricetracker.query.all())
        entry = pricetracker(url=url, name=items[0], price=items[1], date=items[3], time=items[2])
        db.session.add(entry)
        db.session.commit()
        flash("The product has been added to the list", category='success')
    return render_template('show.html', products=pricetracker.query.all())


@view.route("/remove/<id>", methods=['GET', 'POST'])
def delete(id):
    pricetracker.query.filter_by(id=id).delete()
    db.session.commit()
    flash("Product has been removed successfully", category='success')
    return render_template('show.html', products=pricetracker.query.all())


@view.route("/update", methods=['GET', 'POST'])
def update():
    whole_data = pricetracker.query.all()
    for data in whole_data:
        try:
            items = track(data.url)
        except:
            temp = pricetracker.query.filter_by(url = data.url).first()
            temp.price = 0
            temp.name = "Not Available"
            db.session.commit()
            flash("The list has been updated successfully:)", category='success')
            return render_template('show.html', products=pricetracker.query.all())

        temp = pricetracker.query.filter_by(url = data.url).first()
        temp.price = items[1]
        temp.date = items[3]
        temp.time = items[2]
        db.session.commit()
    flash("The list has been updated successfully:)", category='success')
    return render_template('show.html', products=pricetracker.query.all())