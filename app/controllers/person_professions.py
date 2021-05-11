from flask import request
from flask_restx import Resource, fields
import json

from app import api, isOnDev, project_dir
from app.models.person_professions import PersonProfessionModel as TheModel
from app.schemas.person_professions import PersonProfessionSchema as TheSchema
from app.const import *

#   Name of the current item/element
CURRENT_NAME = 'PersonProfession'
CACHE_FILE = "/db/person-profession.json"

#   Namespace to route
local_ns = api.namespace('person-profession', description=CURRENT_NAME + ' related operations')

#   Database schemas
local_schema = TheSchema()

#   Model required by flask_restx for expect on POST and PUT methods
model_validator = local_ns.model(CURRENT_NAME, {
    'person_id': fields.Integer,
    'profession_id': fields.Integer
})

@local_ns.route('/')
class PersonProfessionList(Resource):
    @local_ns.doc('Get all the ' + CURRENT_NAME + 's')
    def get(self):
        try:
            if isOnDev:
                return TheModel.find_all(), HttpStatus.OK
            else:
                f = open(project_dir + CACHE_FILE, "r")
                data_json = json.loads(f.read())
                f.close()
                return data_json, HttpStatus.OK
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Create a ' + CURRENT_NAME)
    @local_ns.expect(model_validator)
    def post(self):
        if not isOnDev:
            return {'message': 'Not allowed'}, HttpStatus.NOT_ALLOWED
        try:
            element_json = request.get_json()
            element_data = local_schema.load(element_json)
            element_data.save()
            return element_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

@local_ns.route('/<int:id>')
class PersonProfession(Resource):
    @local_ns.doc('Get the ' + CURRENT_NAME + ' with the specified id',
                  params={
                    'id': 'id of the ' + CURRENT_NAME + ' to get'
                })
    def get(self, id):
        try:
            element_data = TheModel.find_by_id(id)
            if element_data:
                return element_data.json()
            return {'message': CURRENT_NAME + ' not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Update a ' + CURRENT_NAME + ' with the specified id',
                  params={
                    'id': 'id of the ' + CURRENT_NAME + ' to update'
                })
    @local_ns.expect(model_validator)
    def put(self, id):
        if not isOnDev:
            return {'message': 'Not allowed'}, HttpStatus.NOT_ALLOWED
        try:
            element_data = TheModel.find_by_id(id)

            if element_data:
                element_data.person_id = EmptyValues.EMPTY_INT if request.json['person_id'] == EmptyValues.EMPTY_STRING else request.json['person_id']
                element_data.profession_id = EmptyValues.EMPTY_INT if request.json['profession_id'] == EmptyValues.EMPTY_STRING else request.json['profession_id']
            else:
                return {'message': CURRENT_NAME + ' not found.'}, HttpStatus.NOT_FOUND

            element_data.save()
            return element_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

    @local_ns.doc('Delete a ' + CURRENT_NAME + ' with the specified id',
                  params={
                    'id': 'id of the ' + CURRENT_NAME + ' to delete'
                })
    def delete(self, id):
        if not isOnDev:
            return {'message': 'Not allowed'}, HttpStatus.NOT_ALLOWED
        try:
            element_data = TheModel.find_by_id(id)
            if element_data:
                element_data.delete()
                return {'message': CURRENT_NAME + ' deleted.'}, HttpStatus.OK
            return {'message': CURRENT_NAME + ' not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR