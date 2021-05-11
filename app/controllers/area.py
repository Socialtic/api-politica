from flask import request, jsonify
from flask_restx import Resource, fields
import json

from app import api, isOnDev, project_dir
from app.models.area import AreaModel as TheModel
from app.schemas.area import AreaSchema as TheSchema
from app.const import HttpStatus, EmptyValues

#   Name of the current item/element
CURRENT_NAME = 'Area'
CACHE_FILE = "/db/area.json"

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
            if isOnDev:
                response = jsonify(TheModel.find_all())
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

    @local_ns.doc('Create an ' + CURRENT_NAME)
    @local_ns.expect(model_validator)
    def post(self):
        if not isOnDev:
            response = jsonify({'message': 'Not allowed'})
            response.status_code = HttpStatus.NOT_ALLOWED
            return response
        try:
            element_json = request.get_json()
            element_data = local_schema.load(element_json)
            element_data.save()
            response = jsonify(element_data.json())
            response.status_code = HttpStatus.CREATED
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.BAD_REQUEST
        return response

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
                response = jsonify(element_data.json())
                response.status_code = HttpStatus.OK
            else:
                response = jsonify({'message': CURRENT_NAME + ' not found.'})
                response.status_code = HttpStatus.NOT_FOUND
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.INTERNAL_ERROR
        return response

    @local_ns.doc('Update an ' + CURRENT_NAME + ' with the specified id',
                  params={
                      'id': 'id of the ' + CURRENT_NAME + ' to update'
                  })
    @local_ns.expect(model_validator)
    def put(self, id):
        if not isOnDev:
            response = jsonify({'message': 'Not allowed'})
            response.status_code = HttpStatus.NOT_ALLOWED
            return response
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
                element_data.save()
                response = jsonify(element_data.json())
                response.status_code = HttpStatus.CREATED
            else:
                response = jsonify({'message': CURRENT_NAME + ' not found.'})
                response.status_code = HttpStatus.NOT_FOUND
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.BAD_REQUEST
        return response

    @local_ns.doc('Delete an ' + CURRENT_NAME + ' with the specified id',
                  params={
                      'id': 'id of the ' + CURRENT_NAME + ' to delete'
                  })
    def delete(self, id):
        if not isOnDev:
            response = jsonify({'message': 'Not allowed'})
            response.status_code = HttpStatus.NOT_ALLOWED
            return response
        try:
            element_data = TheModel.find_by_id(id)
            if element_data:
                element_data.delete()
                response = jsonify({'message': CURRENT_NAME + ' deleted.'})
                response.status_code = HttpStatus.OK
            else:
                response = jsonify({'message': CURRENT_NAME + ' not found.'})
                response.status_code = HttpStatus.NOT_FOUND
        except Exception as e:
            response = jsonify({'message': e.__str__()})
            response.status_code = HttpStatus.INTERNAL_ERROR
        return response