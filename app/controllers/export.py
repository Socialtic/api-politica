from flask import jsonify, request
from flask_restx import Resource
from app import api, isOnDev, project_dir, INTERNAL_TOKEN
import json

#   Min
from app.models.area import AreaModel
from app.models.chamber import ChamberModel
from app.models.role import RoleModel
from app.models.person import PersonModel
from app.models.party import PartyModel
from app.models.memberships import MembershipModel
from app.models.contest import ContestModel

#   Extended
from app.models.coalition import CoalitionModel
from app.models.other_names import OtherNamesModel
from app.models.professions import ProfessionModel
from app.models.person_professions import PersonProfessionModel
from app.models.url import UrlModel

from app.const import HttpStatus, EmptyValues

CACHE_FILE = "/db/export.json"
CACHE_FILE_MIN = "/db/export-min.json"

#   Namespace to route
export_ns = api.namespace('export', description='Get all information')
export_min_ns = api.namespace('export-min', description='Get minimum necessary information')

@export_min_ns.route('/')
class ExportMin(Resource):
    @export_min_ns.doc('Get all information')
    def get(self):
        if INTERNAL_TOKEN.compare(request.headers.get('Authorization')):
            try:
                if isOnDev:
                    obj = {
                        'areas': AreaModel.find_all(),
                        'chambers': ChamberModel.find_all(),
                        'roles': RoleModel.find_all(),
                        'persons': PersonModel.find_all(),
                        'parties': PartyModel.find_all(),
                        'memberships': MembershipModel.find_all(),
                        'contests': ContestModel.find_all()
                    }
                    response = jsonify(obj)
                    response.status_code = HttpStatus.OK
                else:
                    f = open(project_dir + CACHE_FILE, "r")
                    data_json = json.loads(f.read())
                    f.close()
                    response = jsonify(data_json)
                    response.status_code = HttpStatus.OK
            except Exception as e:
                response = jsonify({'message': e.__str__()})
                response.status_code = HttpStatus.INTERNAL_ERROR
            return response
        else:
            response = jsonify({'message': 'Unauthorized'})
            response.status_code = HttpStatus.UNAUTHORIZED
            return response

@export_ns.route('/')
class Export(Resource):
    @export_ns.doc('Get minimum necessary information')
    def get(self):
        if INTERNAL_TOKEN.compare(request.headers.get('Authorization')):
            try:
                if isOnDev:
                    obj = {
                        'areas': AreaModel.find_all(),
                        'chambers': ChamberModel.find_all(),
                        'roles': RoleModel.find_all(),
                        'coalitions': CoalitionModel.find_all(),
                        'persons': PersonModel.find_all(),
                        'other-names': OtherNamesModel.find_all(),
                        'professions': ProfessionModel.find_all(),
                        'person-professions': PersonProfessionModel.find_all(),
                        'parties': PartyModel.find_all(),
                        'memberships': MembershipModel.find_all(),
                        'contests': ContestModel.find_all(),
                        'urls': UrlModel.find_all()
                    }
                    response = jsonify(obj)
                    response.status_code = HttpStatus.OK
                else:
                    f = open(project_dir + CACHE_FILE, "r")
                    data_json = json.loads(f.read())
                    f.close()
                    response = jsonify(data_json)
                    response.status_code = HttpStatus.OK
            except Exception as e:
                response = jsonify({'message': e.__str__()})
                response.status_code = HttpStatus.INTERNAL_ERROR
            return response
        else:
            response = jsonify({'message': 'Unauthorized'})
            response.status_code = HttpStatus.UNAUTHORIZED
            return response