from flask import Blueprint, render_template

blueprint = Blueprint(
    'home', __name__, static_folder='../static', template_folder='templates')


@blueprint.route('/')
def index():
    return render_template('home/index.html')
