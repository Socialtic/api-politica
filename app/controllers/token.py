from flask import Blueprint, render_template
from flask import request
import requests
from json2html import *

bp_token = Blueprint('token', __name__, url_prefix='/')

@bp_token.route('/token/')
def token():

    url = 'https://mx-elections-2021-api.auth.us-east-2.amazoncognito.com/oauth2/token'
    authorization_code = request.args.get('code')
    client_id = '6db6blllaim1ebqnefoe61bn9l'
    grant_type = 'authorization_code'
    authorization = 'Basic NmRiNmJsbGxhaW0xZWJxbmVmb2U2MWJuOWw6MWljMWFlcXBkNTRvcTB1cXBuOG1uc2xkNzc4MmpmZ240cW84OGVwdWtmMmptYjI1YmU5ZA=='

    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': authorization,
    }

    body='grant_type=' + grant_type + '&client_id=' + client_id + '&code=' + authorization_code + '&redirect_uri=https://www.apielectoral.mx/token'

    response = requests.request('POST', url, headers=headers, data=body)
    print(response.request.url)
    print(response.request.body)
    print(response.request.headers)

    return render_template('token.html', authorization_code = authorization_code, response = json2html.convert(json = response.json()))
