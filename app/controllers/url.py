from flask import request
from flask_restx import Resource, fields

from app import api
from app.models.url import UrlModel
from app.schemas.url import UrlSchema
from app.const import *

#   Namespace to route
local_ns = api.namespace('url', description='URL related operations')

#   Database schemas
local_schema = UrlSchema()

#   Model required by flask_restx for expect on POST and PUT methods
url = local_ns.model('URL', {
    'url': fields.String,
    'description': fields.String,
    'url_type': fields.Integer,
    'owner_type': fields.Integer,
    'owner_id': fields.Integer
})

@local_ns.route('/')
class UrlList(Resource):
    @local_ns.doc('Get all the URLs')
    def get(self):
        try:
            return UrlModel.find_all(), HttpStatus.OK
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Create an URL')
    @local_ns.expect(url)
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
    @local_ns.doc('Get the URL with the specified id',
                  params={
                    'id': 'id of the URL to get'
                })
    def get(self, id):
        try:
            element_data = UrlModel.find_by_id(id)
            if element_data:
                return element_data.json()
            return {'message': 'URL not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @local_ns.doc('Update an URL with the specified id',
                  params={
                    'id': 'id of the URL to update'
                })
    @local_ns.expect(url)
    def put(self, id):
        try:
            element_data = UrlModel.find_by_id(id)

            if element_data:
                element_data.url = EmptyValues.EMPTY_STRING if request.json['url'] == EmptyValues.EMPTY_STRING else request.json['url']
                element_data.description = EmptyValues.EMPTY_STRING if request.json['description'] == EmptyValues.EMPTY_STRING else request.json['description']
                element_data.url_type = EmptyValues.EMPTY_INT if request.json['url_type'] == EmptyValues.EMPTY_STRING else request.json['url_type']
                element_data.owner_type = EmptyValues.EMPTY_INT if request.json['owner_type'] == EmptyValues.EMPTY_STRING else request.json['owner_type']
                element_data.owner_id = EmptyValues.EMPTY_INT if request.json['owner_id'] == EmptyValues.EMPTY_STRING else request.json['owner_id']
            else:
                return {'message': 'URL not found.'}, HttpStatus.NOT_FOUND

            element_data.save()
            return element_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

    @local_ns.doc('Delete an URL with the specified id',
                  params={
                    'id': 'id of the URL to delete'
                })
    def delete(self, id):
        try:
            element_data = UrlModel.find_by_id(id)
            if element_data:
                element_data.delete()
                return {'message': 'URL deleted.'}, HttpStatus.OK
            return {'message': 'URL not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR