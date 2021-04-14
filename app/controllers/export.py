from flask import request, jsonify
from app import application as app
from app.models.area import *
from app.models.chamber import *
from app.models.role import *
from app.models.person import *
from app.models.party import *
from app.models.memberships import *
from app.models.contest import *
from app.const import *

@app.route('/export', methods=['GET'])
def export():

    construct = {}

    construct = {
        'areas': Area.getAll(),
        'chambers': Chamber.getAll(),
        'roles': Role.getAll(),
        'persons': Person.getAll(),
        'parties': Party.getAll(),
        'memberships': Membership.getAll(),
        'contests': Contest.getAll()
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.OK
    return response