import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:senha@localhost/bd'
    SQLALCHEMY_TRACK_MODIFICATIONS = False