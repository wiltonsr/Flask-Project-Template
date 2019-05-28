from flask import Flask, render_template
from config import Dev, Prod
from project import home


def create_app(conf=None):
    app = Flask(__name__)

    if (conf == 'development'):
        app.config.from_object(Dev)
    elif (conf == 'production'):
        app.config.from_object(Prod)
    else:
        app.config.from_object(Dev)

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)

    return app


def register_extensions(app):
    return None


def register_blueprints(app):
    app.register_blueprint(home.views.blueprint)
    return None


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('error/{0}.html'.format(error_code)), error_code
    for errcode in [403, 404, 405, 413, 500, 502]:
        app.errorhandler(errcode)(render_error)
    return None
