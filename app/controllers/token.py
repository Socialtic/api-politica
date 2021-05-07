from flask import Blueprint, render_template
from flask import request

bp_frontend = Blueprint('token', __name__, url_prefix='/')

@bp_frontend.route('/token')
def token():
    id_token = request.args.get('id_token')
    access_token = request.args.get('access_token')
    return render_template('token.html', access_token = access_token, id_token = id_token)
