from flask import request, jsonify
from app import application as app
from app.models.other_names import *
from app.const import *
from app import isOnDev

@app.route('/other-name', methods=['GET', 'POST'])
def other_names_fun():

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Get all from table other_names
    if request.method == 'GET':
        construct = {
            'success': True,
            'other_names': Other_Names.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST' and isOnDev:

        #   Trying to get parameters from the POST method
        try:
            other_name_type = EmptyValues.EMPTY_INT if request.json['other_name_type'] == EmptyValues.EMPTY_STRING else request.json['other_name_type']
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            person_id = EmptyValues.EMPTY_INT if request.json['person_id'] == EmptyValues.EMPTY_STRING else request.json['person_id']

            #   Verifying REQUIRED values
            if other_name_type == EmptyValues.EMPTY_INT or name == EmptyValues.EMPTY_STRING or person_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for other_name_type, name and person_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                other_name = Other_Names(other_name_type_id=other_name_type, name=name, person_id=person_id)
                other_name.save()
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

@app.route('/other-name/<int:other_name_id>', methods=['GET', 'PUT', 'DELETE'])
def otherNameId(other_name_id):

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Trying to get the area with other_name_id
    other_name = Other_Names.query.filter_by(other_name_id=other_name_id).first()

    #   If theres no result from the above query
    if not other_name:
        construct = {
            'success': False,
            'message': 'Theres no data for that other_name_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'other_name': {
                'id': other_name.other_name_id,
                'other_name_type_id': Catalogues.OTHER_NAMES_TYPES[other_name.other_name_type_id],
                'name': other_name.name,
                'person_id': other_name.person_id
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT' and isOnDev:

        #   Trying to get parameters from the PUT method
        try:
            other_name_type = EmptyValues.EMPTY_INT if request.json['other_name_type'] == EmptyValues.EMPTY_STRING else request.json['other_name_type']
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            person_id = EmptyValues.EMPTY_INT if request.json['person_id'] == EmptyValues.EMPTY_STRING else request.json['person_id']

            #   Verifying REQUIRED values
            if other_name_type == EmptyValues.EMPTY_INT or name == EmptyValues.EMPTY_STRING or person_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for other_name_type, name and person_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                other_name.other_name_type_id = other_name_id
                other_name.name = name
                other_name.person_id = person_id
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
    elif request.method == 'DELETE' and isOnDev:

        try:
            other_name.delete()
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
