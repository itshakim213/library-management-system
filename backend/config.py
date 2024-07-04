import os

class Config:
    SECRET_KEY = os.environ.get('331b716eea5917501963e8f7453b0f19') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///library.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
