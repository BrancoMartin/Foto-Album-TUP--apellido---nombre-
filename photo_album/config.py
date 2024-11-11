import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'una-clave-secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///photo_album.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
