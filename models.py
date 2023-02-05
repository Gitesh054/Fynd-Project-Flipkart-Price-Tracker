from main import db


class pricetracker(db.Model):
    url = db.Column(db.String(2000), primary_key=False, unique=True)
    name = db.Column(db.String(2000), unique=False, nullable=False)
    price = db.Column(db.String(10), unique=False, nullable=False)
    id = db.Column(db.Integer,primary_key=True ,unique=True, nullable=False)
    date = db.Column(db.String(20), unique=False, nullable=False)
    time = db.Column(db.String(20), unique=False, nullable=True)