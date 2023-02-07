from main import db


class pricetracker(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    url = db.Column(db.String(2000), unique=False)
    name = db.Column(db.String(2000), unique=False, nullable=False)
    price = db.Column(db.String(10), unique=False, nullable=False)
    date = db.Column(db.String(20), unique=False, nullable=False)
    time = db.Column(db.String(20), unique=False, nullable=True)