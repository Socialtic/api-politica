from flask import request
from flask_restx import Resource, fields

from app import api, isOnDev
from app.models.party import PartyModel as TheModel
from app.schemas.party import PartySchema as TheSchema
from app.const import HttpStatus, EmptyValues

#   Name of the current item/element
CURRENT_NAME = 'Party'

#   Namespace to route
local_ns = api.namespace('party', description=CURRENT_NAME + ' related operations')

#   Database schemas
local_schema = TheSchema()

#   Model required by flask_restx for expect on POST and PUT methods
model_validator = local_ns.model(CURRENT_NAME, {
    'name': fields.String,
    'abbreviation': fields.String,
    'colors': fields.List(fields.String),
    'area_id': fields.Integer,
    'coalition_id': fields.Integer
})

@local_ns.route('/')
class PartyList(Resource):
    @local_ns.doc('Get all the ' + CURRENT_NAME + 's')
    def get(self):
        try:
            return TheModel.find_all(), HttpStatus.OK
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
class Party(Resource):
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
                element_data.name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
                element_data.abbreviation = EmptyValues.EMPTY_STRING if request.json['abbreviation'] == EmptyValues.EMPTY_STRING else request.json['abbreviation']
                element_data.colors = EmptyValues.EMPTY_STRING if request.json['colors'] == EmptyValues.EMPTY_STRING else request.json['colors']
                element_data.area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
                element_data.coalition_id = EmptyValues.EMPTY_INT if request.json['coalition_id'] == EmptyValues.EMPTY_STRING else request.json['coalition_id']
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