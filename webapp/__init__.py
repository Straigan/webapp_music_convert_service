from flask import Flask
from flask_migrate import Migrate

from webapp.db import db
from webapp.users.models import User
from webapp.music_convert_service.models import Record
from webapp.users.views import blueprint as users
from webapp.music_convert_service.views import blueprint as music_convert_service


def create_webapp():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    Migrate(app, db)
    app.register_blueprint(users)
    app.register_blueprint(music_convert_service)
    with app.app_context():
        db.create_all()
   
    return app

app = create_webapp()