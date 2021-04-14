from flask import request, jsonify
from app import application as app
from app.models.url import *
from app.const import *

@app.route('/url', methods=['GET', 'POST'])
def url_fun():

    construct = {}

    #   Get all from table url
    if request.method == 'GET':
        construct = {
            'success': True,
            'urls': Url.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST':

        #   Trying to get parameters from the POST method
        try:
            url_val = EmptyValues.EMPTY_STRING if request.json['url'] == EmptyValues.EMPTY_STRING else request.json['url']
            description = EmptyValues.EMPTY_STRING if request.json['description'] == EmptyValues.EMPTY_STRING else request.json['description']
            url_type = EmptyValues.EMPTY_INT if request.json['url_type'] == EmptyValues.EMPTY_STRING else request.json['url_type']
            owner_type = EmptyValues.EMPTY_INT if request.json['owner_type'] == EmptyValues.EMPTY_STRING else request.json['owner_type']
            owner_id = EmptyValues.EMPTY_INT if request.json['owner_id'] == EmptyValues.EMPTY_STRING else request.json['owner_id']

            #   Verifying REQUIRED values
            if url_val == EmptyValues.EMPTY_STRING or url_type == EmptyValues.EMPTY_INT or owner_type == EmptyValues.EMPTY_INT or owner_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for url, url_type, owner_type and owner_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                url = Url(
                    url=url_val, description=description, url_type=url_type, owner_type=owner_type, owner_id=owner_id
                )
                url.save()
                construct['success'] = True
                construct['message'] = 'Data saved'
                response = jsonify(construct)
                response.status_code = HttpStatus.CREATED

            #   Falling while INSERTING into the DB
            except Exception as e:
                construct['success'] = False
                construct['error'] = str(e)
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST

        #   Missing parameters from the POST method
        except Exception as e:
            construct['success'] = False
            construct['error'] = 'Missing data. Missing value ' + str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST

    return response

@app.route('/url/<int:url_id>', methods=['GET', 'PUT', 'DELETE'])
def urlId(url_id):

    #   Trying to get the area with area_id
    url = Url.query.filter_by(url_id=url_id).first()

    #   If theres no result from the above query
    if not url:
        construct = {
            'success': False,
            'message': 'Theres no data for that url_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'url': {
                'id': url.url_id,
                'url': url.url,
                'description': url.description,
                'url_type': url.url_type,
                'owner_type': url.owner_type,
                'owner_id': url.owner_id
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT':
        construct = {}

        #   Trying to get parameters from the PUT method
        try:
            url_val = EmptyValues.EMPTY_STRING if request.json['url'] == EmptyValues.EMPTY_STRING else request.json['url']
            description = EmptyValues.EMPTY_STRING if request.json['description'] == EmptyValues.EMPTY_STRING else request.json['description']
            url_type = EmptyValues.EMPTY_INT if request.json['url_type'] == EmptyValues.EMPTY_STRING else request.json['url_type']
            owner_type = EmptyValues.EMPTY_INT if request.json['owner_type'] == EmptyValues.EMPTY_STRING else request.json['owner_type']
            owner_id = EmptyValues.EMPTY_INT if request.json['owner_id'] == EmptyValues.EMPTY_STRING else request.json['owner_id']

            #   Verifying REQUIRED values
            if url_val == EmptyValues.EMPTY_STRING or url_type == EmptyValues.EMPTY_INT or owner_type == EmptyValues.EMPTY_INT or owner_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for url, url_type, owner_type and owner_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                url.url = url_val
                url.description = description
                url.url_type = url_type
                url.owner_type = owner_type
                url.owner_id = owner_id
                db.session.commit()
                construct['success'] = True
                construct['message'] = 'Data saved'
                response = jsonify(construct)
                response.status_code = HttpStatus.CREATED

            #   Falling while UPDATING into the DB
            except Exception as e:
                construct['success'] = False
                construct['error'] = str(e)
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST

        #   Missing parameters from the PUT method
        except Exception as e:
            construct['success'] = False
            construct['error'] = 'Missing data. Missing value ' + str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST

    #   Delete it from the database
    elif request.method == 'DELETE':
        construct = {}
        try:
            url.delete()
            construct['success'] = True
            construct['message'] = 'Data has been delete.'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
    return response
