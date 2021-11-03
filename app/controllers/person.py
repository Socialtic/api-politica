from flask import request, jsonify
from flask_restx import Resource, fields
from datetime import datetime
import json

from app import api, isOnDev, project_dir, INTERNAL_TOKEN
from app.models.person import PersonModel as TheModel
from app.schemas.person import PersonSchema as TheSchema
from app.const import HttpStatus, EmptyValues

#   Name of the current item/element
CURRENT_NAME = 'Person'
CACHE_FILE = "/db/person.json"

#   Namespace to route
local_ns = api.namespace('person', description=CURRENT_NAME + ' related operations')

#   Database schemas
local_schema = TheSchema()

#   Model required by flask_restx for expect on POST and PUT methods
model_validator = local_ns.model(CURRENT_NAME, {
    'dni': fields.String,
    'first_name': fields.String,
    'last_name': fields.String,
    'full_name': fields.String,
    'date_birth': fields.Date,
    'gender': fields.Integer,
    'dead_or_alive': fields.Boolean,
    'last_degree_of_studies': fields.Integer,
    'contest_id': fields.Integer
})

@local_ns.route('/')
class PersonList(Resource):
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
class Person(Resource):
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
                    element_data.first_name = EmptyValues.EMPTY_STRING if request.json['first_name'] == EmptyValues.EMPTY_STRING else request.json['first_name']
                    element_data.last_name = EmptyValues.EMPTY_STRING if request.json['last_name'] == EmptyValues.EMPTY_STRING else request.json['last_name']
                    element_data.full_name = EmptyValues.EMPTY_STRING if request.json['full_name'] == EmptyValues.EMPTY_STRING else request.json['full_name']
                    some_date = EmptyValues.EMPTY_DATE if request.json['date_birth'] == EmptyValues.EMPTY_STRING else request.json['date_birth']
                    element_data.date_birth = datetime.strptime(some_date, '%Y-%m-%d').date()
                    element_data.gender = EmptyValues.EMPTY_INT if request.json['gender'] == EmptyValues.EMPTY_STRING else request.json['gender']
                    element_data.dead_or_alive = EmptyValues.EMPTY_INT if request.json['dead_or_alive'] == EmptyValues.EMPTY_STRING else request.json['dead_or_alive']
                    element_data.last_degree_of_studies = EmptyValues.EMPTY_INT if request.json['last_degree_of_studies'] == EmptyValues.EMPTY_STRING else request.json['last_degree_of_studies']
                    element_data.contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']
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