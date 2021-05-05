from flask import request
from flask_restx import Resource, fields

from app import api
from app.models.url import *
from app.schemas.url import *
from app.const import *

#   Namespace to route
url_ns = api.namespace('url', description='URL related operations')

#   Database schemas
url_schema = UrlSchema()

#   Model required by flask_restx for expect on POST and PUT methods
url = url_ns.model('URL',{
    'url': fields.String,
    'description': fields.String,
    'url_type': fields.Integer,
    'owner_type': fields.Integer,
    'owner_id': fields.Integer
})

@url_ns.route('/')
class UrlList(Resource):
    @url_ns.doc('Get all the URLs')
    def get(self):
        try:
            return UrlModel.find_all(), HttpStatus.OK
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @url_ns.doc('Create an URL')
    @url_ns.expect(url)
    def post(self):
        try:
            url_json = request.get_json()
            url_data = url_schema.load(url_json)
            url_data.save()
            return url_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

@url_ns.route('/<int:id>')
class Url(Resource):
    @url_ns.doc('Get the URL with the specified id',
                params={
                    'id': 'id of the URL to get'
                })
    def get(self, id):
        try:
            url_data = UrlModel.find_by_id(id)
            if url_data:
                return url_data.json()
            return {'message': 'URL not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR

    @url_ns.doc('Update an URL with the specified id',
                params={
                    'id': 'id of the URL to update'
                })
    @url_ns.expect(url)
    def put(self, id):
        try:
            url_data = UrlModel.find_by_id(id)

            if url_data:
                url_data.url = EmptyValues.EMPTY_STRING if request.json['url'] == EmptyValues.EMPTY_STRING else request.json['url']
                url_data.description = EmptyValues.EMPTY_STRING if request.json['description'] == EmptyValues.EMPTY_STRING else request.json['description']
                url_data.url_type = EmptyValues.EMPTY_INT if request.json['url_type'] == EmptyValues.EMPTY_STRING else request.json['url_type']
                url_data.owner_type = EmptyValues.EMPTY_INT if request.json['owner_type'] == EmptyValues.EMPTY_STRING else request.json['owner_type']
                url_data.owner_id = EmptyValues.EMPTY_INT if request.json['owner_id'] == EmptyValues.EMPTY_STRING else request.json['owner_id']
            else:
                return {'message': 'URL not found.'}, HttpStatus.NOT_FOUND

            url_data.save()
            return url_data.json(), HttpStatus.CREATED
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.BAD_REQUEST

    @url_ns.doc('Delete an URL with the specified id',
                params={
                    'id': 'id of the URL to delete'
                })
    def delete(self, id):
        try:
            url_data = UrlModel.find_by_id(id)
            if url_data:
                url_data.delete()
                return {'message': 'URL deleted.'}, HttpStatus.OK
            return {'message': 'URL not found.'}, HttpStatus.NOT_FOUND
        except Exception as e:
            return {'message': e.__str__()}, HttpStatus.INTERNAL_ERROR