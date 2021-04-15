from flask import request, jsonify
from app import application as app
from app.models.person_professions import *
from app.const import *
from app import isOnDev

@app.route('/person-profession', methods=['GET', 'POST'])
def person_profession_fun():

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Get all from table person_professions
    if request.method == 'GET':
        construct = {
            'success': True,
            'person-professions': Person_Profession.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST' and isOnDev:

        #   Trying to get parameters from the POST method
        try:
            person_id = EmptyValues.EMPTY_INT if request.json['person_id'] == EmptyValues.EMPTY_STRING else request.json['person_id']
            profession_id = EmptyValues.EMPTY_INT if request.json['profession_id'] == EmptyValues.EMPTY_STRING else request.json['profession_id']

            #   Verifying REQUIRED values
            if person_id == EmptyValues.EMPTY_INT or profession_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required value for person_id and profession_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                person_profession = Person_Profession(person_id=person_id, profession_id=profession_id)
                person_profession.save()
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

@app.route('/person-profession/<int:person_profession_id>', methods=['GET', 'PUT', 'DELETE'])
def personProfessionID(person_profession_id):

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Trying to get the area with person_profession_id
    person_profession = Person_Profession.query.filter_by(person_profession_id=person_profession_id).first()

    #   If theres no result from the above query
    if not person_profession:
        construct = {
            'success': False,
            'message': 'Theres no data for that person_profession_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'person_profession': {
                'id': person_profession.person_profession_id,
                'person_id': person_profession.person_id,
                'profession_id': person_profession.profession_id
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT' and isOnDev:

        #   Trying to get parameters from the PUT method
        try:
            person_id = EmptyValues.EMPTY_INT if request.json['person_id'] == EmptyValues.EMPTY_STRING else request.json['person_id']
            profession_id = EmptyValues.EMPTY_INT if request.json['profession_id'] == EmptyValues.EMPTY_STRING else request.json['profession_id']

            #   Verifying REQUIRED values
            if person_id == EmptyValues.EMPTY_INT or profession_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required value for person_id and profession_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                person_profession.person_id = person_id
                person_profession.profession_id = profession_id
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
            person_profession.delete()
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
