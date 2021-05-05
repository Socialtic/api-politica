from flask import request
from flask_restx import Resource, fields

from app import api
from app.models.role import RoleModel
from app.schemas.role import RoleSchema
from app.const import *

#   Namespace to route
local_ns = api.namespace('role', description='Role related operations')

#   Database schemas
local_schema = RoleSchema()

#   Model required by flask_restx for expect on POST and PUT methods
role = local_ns.model('Role', {
    'title': fields.String,
    'role': fields.Integer,
    'area_id': fields.Integer,
    'chamber_id': fields.Integer,
    'contest_id': fields.Integer
})

@local_ns.route('/')
class RoleList(Resource):
    @local_ns.doc('Get all the Roles')
    def get(self):
        try:
            return RoleModel.find_all(), HttpStatus.OK
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Create a Role')
    @local_ns.expect(role)
    def post(self):
        try:
            element_json = request.get_json()
            element_data = local_schema.load(element_json)
            element_data.save()
            return element_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

@local_ns.route('/<int:id>')
class Role(Resource):
    @local_ns.doc('Get the Role with the specified id',
                  params={
                    'id': 'id of the Role to get'
                })
    def get(self, id):
        try:
            element_data = RoleModel.find_by_id(id)
            if element_data:
                return element_data.json()
            return {'message': 'Role not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Update an Role with the specified id',
                  params={
                    'id': 'id of the Role to update'
                })
    @local_ns.expect(role)
    def put(self, id):
        try:
            element_data = RoleModel.find_by_id(id)

            if element_data:
                element_data.title = EmptyValues.EMPTY_STRING if request.json['title'] == EmptyValues.EMPTY_STRING else request.json['title']
                element_data.role = EmptyValues.EMPTY_INT if request.json['role'] == EmptyValues.EMPTY_STRING else request.json['role']
                element_data.area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
                element_data.chamber_id = EmptyValues.EMPTY_INT if request.json['chamber_id'] == EmptyValues.EMPTY_STRING else request.json['chamber_id']
                element_data.contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']
            else:
                return {'message': 'Role not found.'}, HttpStatus.NOT_FOUND

            element_data.save()
            return element_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

    @local_ns.doc('Delete a Role with the specified id',
                  params={
                    'id': 'id of the Role to delete'
                })
    def delete(self, id):
        try:
            element_data = RoleModel.find_by_id(id)
            if element_data:
                element_data.delete()
                return {'message': 'Role deleted.'}, HttpStatus.OK
            return {'message': 'Role not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR