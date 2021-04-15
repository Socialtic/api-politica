from flask import request, jsonify
from app import application as app

#   Min
from app.models.area import *
from app.models.chamber import *
from app.models.role import *
from app.models.person import *
from app.models.party import *
from app.models.memberships import *
from app.models.contest import *

#   Extended
from app.models.coalition import *
from app.models.other_names import *
from app.models.professions import *
from app.models.person_professions import *
from app.models.url import *

from app.const import *

@app.route('/export-min', methods=['GET'])
def export_min():

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

@app.route('/export', methods=['GET'])
def export():

    construct = {}

    construct = {
        'areas': Area.getAll(),
        'chambers': Chamber.getAll(),
        'roles': Role.getAll(),
        'coalitions': Coalition.getAll(),
        'persons': Person.getAll(),
        'other-names': Other_Names.getAll(),
        'professions': Profession.getAll(),
        'person-professions': Person_Profession.getAll(),
        'parties': Party.getAll(),
        'memberships': Membership.getAll(),
        'contests': Contest.getAll(),
        'urls': Url.getAll()
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.OK
    return response