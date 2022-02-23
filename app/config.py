

import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or '79537d00f4834892986f09a100aa1edf'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

