import os

from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

# WebApp Config
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = 'webapp/static/music/wav'
DOWNLOAD_FOLDER = 'webapp/static/music/mp3'
UPLOAD_ALLOWED_EXTENSIONS = {'wav'}