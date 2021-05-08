from flask import Blueprint, render_template
from flask import request
import requests

bp_token = Blueprint('token', __name__, url_prefix='/')

@bp_token.route('/token/')
def token():

    url = 'https://mx-elections-2021-api.auth.us-east-2.amazoncognito.com'
    authorization_code = request.args.get('code')
    client_id = '6db6blllaim1ebqnefoe61bn9l'
    grant_type = 'authorization_code'


    response = requests.post(url + '/oauth2/token',{'Content-Type':'application/x-www-form-urlencoded', 'grant_type': grant_type, 'client_id': client_id, 'code': authorization_code, 'redirect_uri': 'https://www.candidaturas.mx/token'})


    return render_template('token.html', response_json = response.json())
