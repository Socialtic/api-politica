from flask import request, jsonify
from app import app
from app.models.coalition import *
from app.const import *
from app.controllers.url import *

@app.route('/coalition', methods=['GET', 'POST'])
def coalition():

    construct = {}

    #   Get all from table coalition
    if request.method == 'GET':
        construct = {
            'success': True,
            'coalitions': Coalition.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST':

        #   Trying to get parameters from the POST method
        try:
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            abbreviation = EmptyValues.EMPTY_STRING if request.json['abbreviation'] == EmptyValues.EMPTY_STRING else request.json['abbreviation']
            colors = EmptyValues.EMPTY_STRING if request.json['colors'] == EmptyValues.EMPTY_STRING else request.json['colors']

            #   Verifying REQUIRED values
            if name == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for name.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                coalition = Coalition(
                    name=name, abbreviation=abbreviation, colors=colors
                )
                coalition.save()
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

@app.route('/coalition/<int:coalition_id>', methods=['GET', 'PUT', 'DELETE'])
def coalitionId(coalition_id):

    #   Trying to get the area with area_id
    coalition = Coalition.query.filter_by(coalition_id=coalition_id).first()

    #   If theres no result from the above query
    if not coalition:
        construct = {
            'success': False,
            'message': 'Theres no data for that coalition_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'coalition': {
                'id': coalition.coalition_id,
                'name': coalition.name,
                'abbreviation': coalition.abbreviation,
                'colors': coalition.colors,
                'fb_urls': Url.get_party_or_coalition_fb_urls(coalition.coalition_id, URL_OWNER_TYPE.COALITION),
                'ig_urls': Url.get_party_or_coalition_ig_urls(coalition.coalition_id, URL_OWNER_TYPE.COALITION),
                'logo_urls': Url.get_party_or_coalition_logo_urls(coalition.coalition_id, URL_OWNER_TYPE.COALITION),
                'websites': Url.get_party_or_coalition_or_person_websites_urls(coalition.coalition_id,
                                                                               URL_OWNER_TYPE.COALITION)
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT':
        construct = {}

        #   Trying to get parameters from the PUT method
        try:
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            abbreviation = EmptyValues.EMPTY_STRING if request.json['abbreviation'] == EmptyValues.EMPTY_STRING else request.json['abbreviation']
            colors = EmptyValues.EMPTY_STRING if request.json['colors'] == EmptyValues.EMPTY_STRING else request.json['colors']

            #   Verifying REQUIRED values
            if name == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for name.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                coalition.name = name
                coalition.abbreviation = abbreviation
                coalition.colors = colors
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
            coalition.delete()
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
