from flask import request
from flask_restx import Resource, fields
from datetime import datetime

from app import api, isOnDev
from app.models.contest import ContestModel as TheModel
from app.schemas.contest import ContestSchema as TheSchema
from app.const import HttpStatus, EmptyValues

#   Name of the current item/element
CURRENT_NAME = 'Contest'

#   Namespace to route
local_ns = api.namespace('contest', description=CURRENT_NAME + ' related operations')

#   Database schemas
local_schema = TheSchema()

#   Model required by flask_restx for expect on POST and PUT methods
model_validator = local_ns.model(CURRENT_NAME, {
    'area_id': fields.Integer,
    'title': fields.String,
    'membership_id_winner': fields.Integer,
    'start_date': fields.Date,
    'end_date': fields.Date,
    'election_identifier': fields.String
})

@local_ns.route('/')
class ContestList(Resource):
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
class Contest(Resource):
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
                element_data.area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
                element_data.title = EmptyValues.EMPTY_STRING if request.json['title'] == EmptyValues.EMPTY_STRING else request.json['title']
                element_data.membership_id_winner = EmptyValues.EMPTY_INT if request.json['membership_id_winner'] == EmptyValues.EMPTY_STRING else request.json['membership_id_winner']
                some_start_date = EmptyValues.EMPTY_DATE if request.json['start_date'] == EmptyValues.EMPTY_STRING else request.json['start_date']
                element_data.start_date = datetime.strptime(some_start_date, '%Y-%m-%d')
                some_end_date = EmptyValues.EMPTY_DATE if request.json['end_date'] == EmptyValues.EMPTY_STRING else request.json['end_date']
                element_data.end_date = datetime.strptime(some_end_date, '%Y-%m-%d')
                element_data.election_identifier = EmptyValues.EMPTY_STRING if request.json['election_identifier'] == EmptyValues.EMPTY_STRING else request.json['election_identifier']
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