from flask import request, jsonify
from app import application as app
from app.models.chamber import *
from app.const import *
from app import isOnDev

@app.route('/chamber', methods=['GET', 'POST'])
def chamber():

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Get all from table chamber
    if request.method == 'GET':
        construct = {
            'success': True,
            'chambers': Chamber.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST' and isOnDev:

        #   Trying to get parameters from the POST method
        try:
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']

            #   Verifying REQUIRED values
            if name == EmptyValues.EMPTY_STRING or area_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for name and area_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                chamber = Chamber(name=name, area_id=area_id)
                chamber.save()
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

@app.route('/chamber/<int:chamber_id>', methods=['GET', 'PUT', 'DELETE'])
def chamberId(chamber_id):

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Trying to get the chamber with chamber_id
    chamber = Chamber.query.filter_by(chamber_id=chamber_id).first()

    #   If theres no result from the above query
    if not chamber:
        construct = {
            'success': False,
            'message': 'Theres no data for that chamber_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'chamber': {
                'id': chamber.chamber_id,
                'name': {
                    'en_US': chamber.name
                },
                'area_id': chamber.area_id
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT' and isOnDev:
        construct = {}

        #   Trying to get parameters from the PUT method
        try:
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']

            #   Verifying REQUIRED values
            if name == EmptyValues.EMPTY_STRING or area_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for name and area_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                chamber.name = name
                chamber.area_id = area_id
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
        construct = {}
        try:
            chamber.delete()
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
