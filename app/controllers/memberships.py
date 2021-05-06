from flask import request
from flask_restx import Resource, fields
from datetime import datetime

from app import api
from app.models.memberships import MembershipModel as TheModel
from app.schemas.membserhips import MembershipSchema as TheSchema
from app.const import HttpStatus, EmptyValues
from datetime import date

#   Name of the current item/element
CURRENT_NAME = 'Membership'

#   Namespace to route
local_ns = api.namespace('membership', description=CURRENT_NAME + ' related operations')

#   Database schemas
local_schema = TheSchema()

#   Model required by flask_restx for expect on POST and PUT methods
model_validator = local_ns.model(CURRENT_NAME, {
    'person_id': fields.Integer,
    'role_id': fields.Integer,
    'party_id': fields.Integer,
    'coalition_id': fields.Integer,
    'contest_id': fields.Integer,
    'goes_for_coalition': fields.Boolean,
    'membership_type': fields.Integer,
    'goes_for_reelection': fields.Boolean,
    'start_date': fields.Date,
    'end_date': fields.Date,
    'is_substitute': fields.Boolean,
    'parent_membership_id': fields.Integer,
    'changed_from_substitute': fields.Boolean,
    'date_changed_from_substitute': fields.Date
})

@local_ns.route('/')
class UrlList(Resource):
    @local_ns.doc('Get all the ' + CURRENT_NAME + 's')
    def get(self):
        try:
            return TheModel.find_all(), HttpStatus.OK
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Create a ' + CURRENT_NAME)
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
class Url(Resource):
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
        try:
            element_data = TheModel.find_by_id(id)

            if element_data:
                element_data.person_id = EmptyValues.EMPTY_INT if request.json['person_id'] == EmptyValues.EMPTY_STRING else request.json['person_id']
                element_data.role_id = EmptyValues.EMPTY_INT if request.json['role_id'] == EmptyValues.EMPTY_STRING else request.json['role_id']
                element_data.party_id = EmptyValues.EMPTY_INT if request.json['party_id'] == EmptyValues.EMPTY_STRING else request.json['party_id']
                element_data.coalition_id = EmptyValues.EMPTY_INT if request.json['coalition_id'] == EmptyValues.EMPTY_STRING else request.json['coalition_id']
                element_data.contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']
                element_data.goes_for_coalition = EmptyValues.EMPTY_INT if request.json['goes_for_coalition'] == EmptyValues.EMPTY_STRING else request.json['goes_for_coalition']
                element_data.membership_type = EmptyValues.EMPTY_INT if request.json['membership_type'] == EmptyValues.EMPTY_STRING else request.json['membership_type']
                element_data.goes_for_reelection = EmptyValues.EMPTY_INT if request.json['goes_for_reelection'] == EmptyValues.EMPTY_STRING else request.json['goes_for_reelection']
                some_start_date = EmptyValues.EMPTY_DATE if request.json['start_date'] == EmptyValues.EMPTY_STRING else request.json['start_date']
                element_data.start_date = datetime.strptime(some_start_date, '%Y-%m-%d').date()
                some_end_date = EmptyValues.EMPTY_DATE if request.json['end_date'] == EmptyValues.EMPTY_STRING else request.json['end_date']
                element_data.end_date = datetime.strptime(some_end_date, '%Y-%m-%d').date()
                element_data.is_substitute = EmptyValues.EMPTY_INT if request.json['is_substitute'] == EmptyValues.EMPTY_STRING else request.json['is_substitute']
                element_data.parent_membership_id = EmptyValues.EMPTY_INT if request.json['parent_membership_id'] == EmptyValues.EMPTY_STRING else request.json['parent_membership_id']
                element_data.changed_from_substitute = EmptyValues.EMPTY_INT if request.json['changed_from_substitute'] == EmptyValues.EMPTY_STRING else request.json['changed_from_substitute']
                some_date_changed_from_substitute = EmptyValues.EMPTY_DATE if request.json['date_changed_from_substitute'] == EmptyValues.EMPTY_STRING else request.json['date_changed_from_substitute']
                element_data.date_changed_from_substitute = datetime.strptime(some_date_changed_from_substitute, '%Y-%m-%d').date()
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
        try:
            element_data = TheModel.find_by_id(id)
            if element_data:
                element_data.delete()
                return {'message': CURRENT_NAME + ' deleted.'}, HttpStatus.OK
            return {'message': CURRENT_NAME + ' not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR