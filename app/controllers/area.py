from flask import request
from flask_restx import Resource, fields

from app import api
from app.models.area import AreaModel as TheModel
from app.schemas.area import AreaSchema as TheSchema
from app.const import HttpStatus, EmptyValues

#   Name of the current item/element
CURRENT_NAME = 'Area'

#   Namespace to route
local_ns = api.namespace('area', description=CURRENT_NAME + ' related operations')

#   Database schemas
local_schema = TheSchema()

#   Model required by flask_restx for expect on POST and PUT methods
model_validator = local_ns.model(CURRENT_NAME, {
    'ocd_id': fields.String,
    'name': fields.String,
    'country': fields.String,
    'state': fields.String,
    'city': fields.String,
    'district_type': fields.Integer,
    'parent_area_id': fields.Integer
})

@local_ns.route('/')
class AreaList(Resource):
    @local_ns.doc('Get all the ' + CURRENT_NAME + 's')
    def get(self):
        try:
            return TheModel.find_all(), HttpStatus.OK
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Create an ' + CURRENT_NAME)
    @local_ns.expect(model_validator)
    def post(self):
        try:
            element_json = request.get_json()
            element_data = local_schema.load(element_json)
            element_data.save()
            return element_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

@local_ns.route('/<int:id>')
class Area(Resource):
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

    @local_ns.doc('Update an ' + CURRENT_NAME + ' with the specified id',
                  params={
                    'id': 'id of the ' + CURRENT_NAME + ' to update'
                })
    @local_ns.expect(model_validator)
    def put(self, id):
        try:
            element_data = TheModel.find_by_id(id)

            if element_data:
                element_data.ocd_id = EmptyValues.EMPTY_STRING if request.json['ocd_id'] == EmptyValues.EMPTY_STRING else request.json['ocd_id']
                element_data.name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
                element_data.country = EmptyValues.EMPTY_STRING if request.json['country'] == EmptyValues.EMPTY_STRING else request.json['country']
                element_data.state = EmptyValues.EMPTY_STRING if request.json['state'] == EmptyValues.EMPTY_STRING else request.json['state']
                element_data.city = EmptyValues.EMPTY_STRING if request.json['city'] == EmptyValues.EMPTY_STRING else request.json['city']
                element_data.district_type = EmptyValues.EMPTY_INT if request.json['district_type'] == EmptyValues.EMPTY_STRING else request.json['district_type']
                element_data.parent_area_id = EmptyValues.EMPTY_INT if request.json['parent_area_id'] == EmptyValues.EMPTY_STRING else request.json['parent_area_id']
            else:
                return {'message': CURRENT_NAME + ' not found.'}, HttpStatus.NOT_FOUND

            element_data.save()
            return element_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

    @local_ns.doc('Delete an ' + CURRENT_NAME + ' with the specified id',
                  params={
                    'id': 'id of the ' + CURRENT_NAME + ' to delete'
                })
    def delete(self, id):
        try:
            element_data = TheModel.find_by_id(id)
            if element_data:
                element_data.delete()
                return {'message': CURRENT_NAME + ' deleted.'}, HttpStatus.OK
            return {'message': CURRENT_NAME + ' not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR