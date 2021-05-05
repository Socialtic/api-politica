from flask import request
from flask_restx import Resource, fields

from app import api
from app.models.role import RoleModel
from app.schemas.role import RoleSchema
from app.const import *

#   Namespace to route
role_ns = api.namespace('role', description='Role related operations')

#   Database schemas
role_schema = RoleSchema()

#   Model required by flask_restx for expect on POST and PUT methods
role = role_ns.model('Role',{
    'title': fields.String,
    'role': fields.Integer,
    'area_id': fields.Integer,
    'chamber_id': fields.Integer,
    'contest_id': fields.Integer
})

@role_ns.route('/')
class RoleList(Resource):
    @role_ns.doc('Get all the Roles')
    def get(self):
        try:
            return RoleModel.find_all(), HttpStatus.OK
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @role_ns.doc('Create a Role')
    @role_ns.expect(role)
    def post(self):
        try:
            role_json = request.get_json()
            role_data = role_schema.load(role_json)
            role_data.save()
            return role_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

@role_ns.route('/<int:id>')
class Role(Resource):
    @role_ns.doc('Get the Role with the specified id',
                params={
                    'id': 'id of the Role to get'
                })
    def get(self, id):
        try:
            role_data = RoleModel.find_by_id(id)
            if role_data:
                return role_data.json()
            return {'message': 'Role not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @role_ns.doc('Update an Role with the specified id',
                params={
                    'id': 'id of the Role to update'
                })
    @role_ns.expect(role)
    def put(self, id):
        try:
            role_data = RoleModel.find_by_id(id)

            if role_data:
                role_data.title = EmptyValues.EMPTY_STRING if request.json['title'] == EmptyValues.EMPTY_STRING else request.json['title']
                role_data.role = EmptyValues.EMPTY_INT if request.json['role'] == EmptyValues.EMPTY_STRING else request.json['role']
                role_data.area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
                role_data.chamber_id = EmptyValues.EMPTY_INT if request.json['chamber_id'] == EmptyValues.EMPTY_STRING else request.json['chamber_id']
                role_data.contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']
            else:
                return {'message': 'Role not found.'}, HttpStatus.NOT_FOUND

            role_data.save()
            return role_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

    @role_ns.doc('Delete a Role with the specified id',
                params={
                    'id': 'id of the Role to delete'
                })
    def delete(self, id):
        try:
            role_data = RoleModel.find_by_id(id)
            if role_data:
                role_data.delete()
                return {'message': 'Role deleted.'}, HttpStatus.OK
            return {'message': 'Role not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR