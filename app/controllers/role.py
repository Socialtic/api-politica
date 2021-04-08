from flask import request, jsonify
from app import app
from app.models.role import *
from app.const import *

@app.route('/role', methods=['GET', 'POST'])
def role():
    construct = {}

    #   Get all from table role
    if request.method == 'GET':
        construct = {
            'success': True,
            'roles': Role.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST':

        #   Trying to get parameters from the POST method
        try:
            title = EmptyValues.EMPTY_STRING if request.json['title'] == EmptyValues.EMPTY_STRING else request.json['title']
            role_type = EmptyValues.EMPTY_INT if request.json['role'] == EmptyValues.EMPTY_STRING else request.json['role']
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
            chamber_id = EmptyValues.EMPTY_INT if request.json['chamber_id'] == EmptyValues.EMPTY_STRING else request.json['chamber_id']
            contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']

            #   Verifying REQUIRED values
            if title == EmptyValues.EMPTY_STRING or role_type == EmptyValues.EMPTY_INT or area_id == EmptyValues.EMPTY_INT or chamber_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for title, role, parent_area_id, chamber_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                role = Role(
                    title=title, role_type=role_type, area_id=area_id, chamber_id=chamber_id,
                    contest_id=contest_id
                )
                role.save()
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

@app.route('/role/<int:role_id>', methods=['GET', 'PUT', 'DELETE'])
def roleId(role_id):

    #   Trying to get the role with role_id
    role = Role.query.filter_by(role_id=role_id).first()

    #   If theres no result from the above query
    if not role:
        construct = {
            'success': False,
            'message': 'Theres no data for that role_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'role': {
                'id': role.role_id,
                'title': {
                    'en_US': role.title
                },
                'role': Catalogues.ROLE_TYPES[role.role_type],
                'area_id': role.area_id,
                'chamber_id': role.chamber_id,
                'contest_id': "" if role.contest_id == EmptyValues.EMPTY_INT else role.contest_id
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT':
        construct = {}

        #   Trying to get parameters from the PUT method
        try:
            title = EmptyValues.EMPTY_STRING if request.json['title'] == EmptyValues.EMPTY_STRING else request.json['title']
            role_type = EmptyValues.EMPTY_INT if request.json['role'] == EmptyValues.EMPTY_STRING else request.json['role']
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
            chamber_id = EmptyValues.EMPTY_INT if request.json['chamber_id'] == EmptyValues.EMPTY_STRING else request.json['chamber_id']
            contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']

            #   Verifying REQUIRED values
            if title == EmptyValues.EMPTY_STRING or role_type == EmptyValues.EMPTY_INT or area_id == EmptyValues.EMPTY_INT or chamber_id == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for title, role, parent_area_id, chamber_id.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                role.title = title
                role.role_type = role_type
                role.area_id = area_id
                role.chamber_id = chamber_id
                role.contest_id = contest_id
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
            role.delete()
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
