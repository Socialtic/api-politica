from flask import Blueprint, render_template

bp_frontend = Blueprint('index', __name__, url_prefix='/')

@bp_frontend.route('/')
def index():
    return render_template('index.html')

@bp_frontend.route('/changelog/')
def changelog():
    return render_template('changelog.html')
