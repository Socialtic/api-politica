from flask import request, jsonify
from flask_restx import Resource, fields
import json

from app import api, isOnDev, project_dir, INTERNAL_TOKEN
from app.models.chamber import ChamberModel as TheModel
from app.schemas.chamber import ChamberSchema as TheSchema
from app.const import HttpStatus, EmptyValues

#   Name of the current item/element
CURRENT_NAME = 'Chamber'
CACHE_FILE = "/db/chamber.json"

#   Namespace to route
local_ns = api.namespace('chamber', description=CURRENT_NAME + ' related operations')

#   Database schemas
local_schema = TheSchema()

#   Model required by flask_restx for expect on POST and PUT methods
model_validator = local_ns.model(CURRENT_NAME, {
    'name': fields.String,
    'area_id': fields.Integer
})


@local_ns.route('/')
class ChamberList(Resource):
    @local_ns.doc('Get all the ' + CURRENT_NAME + 's')
    def get(self):
        if INTERNAL_TOKEN.compare(request.headers.get('Authorization')):
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
        else:
            response = jsonify({'message': 'Unauthorized'})
            response.status_code = HttpStatus.UNAUTHORIZED
            return response

    @local_ns.doc('Create a ' + CURRENT_NAME)
    @local_ns.expect(model_validator)
    def post(self):
        if INTERNAL_TOKEN.compare(request.headers.get('Authorization')):
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
        else:
            response = jsonify({'message': 'Unauthorized'})
            response.status_code = HttpStatus.UNAUTHORIZED
            return response


@local_ns.route('/<int:id>')
class Chamber(Resource):
    @local_ns.doc('Get the ' + CURRENT_NAME + ' with the specified id',
                  params={
                      'id': 'id of the ' + CURRENT_NAME + ' to get'
                  })
    def get(self, id):
        if INTERNAL_TOKEN.compare(request.headers.get('Authorization')):
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
        else:
            response = jsonify({'message': 'Unauthorized'})
            response.status_code = HttpStatus.UNAUTHORIZED
            return response

    @local_ns.doc('Update a ' + CURRENT_NAME + ' with the specified id',
                  params={
                      'id': 'id of the ' + CURRENT_NAME + ' to update'
                  })
    @local_ns.expect(model_validator)
    def put(self, id):
        if INTERNAL_TOKEN.compare(request.headers.get('Authorization')):
            if not isOnDev:
                response = jsonify({'message': 'Not allowed'})
                response.status_code = HttpStatus.NOT_ALLOWED
                return response
            try:
                element_data = TheModel.find_by_id(id)

                if element_data:
                    element_data.name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else \
                    request.json['name']
                    element_data.area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else \
                    request.json['area_id']
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
        else:
            response = jsonify({'message': 'Unauthorized'})
            response.status_code = HttpStatus.UNAUTHORIZED
            return response

    @local_ns.doc('Delete a ' + CURRENT_NAME + ' with the specified id',
                  params={
                      'id': 'id of the ' + CURRENT_NAME + ' to delete'
                  })
    def delete(self, id):
        if INTERNAL_TOKEN.compare(request.headers.get('Authorization')):
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
        else:
            response = jsonify({'message': 'Unauthorized'})
            response.status_code = HttpStatus.UNAUTHORIZED
            return response
