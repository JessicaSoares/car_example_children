import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:3012@localhost/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False