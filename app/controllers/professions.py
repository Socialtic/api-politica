from flask import request
from flask_restx import Resource, fields

from app import api
from app.models.professions import ProfessionModel
from app.schemas.professions import ProfessionSchema
from app.const import *

#   Namespace to route
local_ns = api.namespace('profession', description='Profession related operations')

#   Database schemas
local_schema = ProfessionSchema()

#   Model required by flask_restx for expect on POST and PUT methods
profession = local_ns.model('Profession', {
    'description': fields.String
})

@local_ns.route('/')
class ProfessionList(Resource):
    @local_ns.doc('Get all the Professions')
    def get(self):
        try:
            return ProfessionModel.find_all(), HttpStatus.OK
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Create a Profession')
    @local_ns.expect(profession)
    def post(self):
        try:
            element_json = request.get_json()
            element_data = local_schema.load(element_json)
            element_data.save()
            return element_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

@local_ns.route('/<int:id>')
class Profession(Resource):
    @local_ns.doc('Get the Profession with the specified id',
                  params={
                    'id': 'id of the Profession to get'
                })
    def get(self, id):
        try:
            element_data = ProfessionModel.find_by_id(id)
            if element_data:
                return element_data.json()
            return {'message': 'Profession not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Update a Profession with the specified id',
                  params={
                    'id': 'id of the Profession to update'
                })
    @local_ns.expect(profession)
    def put(self, id):
        try:
            element_data = ProfessionModel.find_by_id(id)

            if element_data:
                element_data.description = EmptyValues.EMPTY_STRING if request.json['description'] == EmptyValues.EMPTY_STRING else request.json['description']
            else:
                return {'message': 'Profession not found.'}, HttpStatus.NOT_FOUND

            element_data.save()
            return element_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

    @local_ns.doc('Delete a Profession with the specified id',
                  params={
                    'id': 'id of the Profession to delete'
                })
    def delete(self, id):
        try:
            element_data = ProfessionModel.find_by_id(id)
            if element_data:
                element_data.delete()
                return {'message': 'Profession deleted.'}, HttpStatus.OK
            return {'message': 'Profession not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR