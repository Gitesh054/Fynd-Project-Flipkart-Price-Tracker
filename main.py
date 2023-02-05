from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Gitesh123@127.0.0.1:3306/temp'
    app.secret_key = "super secret key"
    db.init_app(app)
    from views import view
    app.register_blueprint(view, url_prefix="/")
    return app
