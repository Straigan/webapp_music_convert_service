from flask import Flask
from flask_migrate import Migrate

from webapp.db import db
from webapp.users.models import User


def create_webapp():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    Migrate(app, db)
    with app.app_context():
        db.create_all()
   
    return app

app = create_webapp()