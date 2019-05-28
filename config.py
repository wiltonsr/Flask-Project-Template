import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    # Server
    SITEMAP_URL_SCHEME = 'https'
    SECRET_KEY = "you-will-never-guess"


class Prod(BaseConfig):
    # Server
    SERVER_NAME = "example.com"
    PREFERRED_URL_SCHEME = "https"
    DEBUG = False
    TESTING = False
    FLASK_ENV = "production"
    ENV = "production"


class Dev(BaseConfig):
    # Server
    SERVER_NAME = "dev.flask:5000"
    PREFERRED_URL_SCHEME = "http"
    DEBUG = True
    TESTING = True
    FLASK_ENV = "development"
    ENV = "development"
