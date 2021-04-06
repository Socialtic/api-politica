from flask import request, jsonify
from app import app
from app.models.party import *
from app.const import *

@app.route('/party', methods=['GET', 'POST'])
def party():

    construct = {}

    #   Get all from table party
    if request.method == 'GET':
        construct = {
            'success': True,
            'parties': Party.getAll()
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
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
            coalition_id = EmptyValues.EMPTY_INT if request.json['coalition_id'] == EmptyValues.EMPTY_STRING else request.json['coalition_id']

            #   Verifying REQUIRED values
            if name == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for name.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                party = Party(
                    name=name, abbreviation=abbreviation, colors=colors,
                    area_id=area_id, coalition_id=coalition_id
                )
                party.save()
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

@app.route('/party/<int:party_id>', methods=['GET', 'PUT', 'DELETE'])
def partyId(party_id):

    #   Trying to get the area with area_id
    party = Party.query.filter_by(party_id=party_id).first()

    #   If theres no result from the above query
    if not party:
        construct = {
            'success': False,
            'message': 'Theres no data for that party_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'parties': {
                'party_id': party.party_id,
                'name': party.name,
                'abbreviation': party.abbreviation,
                'colors': party.colors,
                'area_id': party.area_id,
                'coalition_id': party.coalition_id
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
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
            coalition_id = EmptyValues.EMPTY_INT if request.json['coalition_id'] == EmptyValues.EMPTY_STRING else request.json['coalition_id']

            #   Verifying REQUIRED values
            if name == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for name.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                party.name = name
                party.abbreviation = abbreviation
                party.colors = colors
                party.area_id = area_id
                party.coalition_id = coalition_id
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
            party.delete()
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
