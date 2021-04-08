from flask import request, jsonify
from app import app
from app.models.past_memberships import *
from app.const import *
from datetime import date

@app.route('/past-membership', methods=['GET', 'POST'])
def pastMembership():

    construct = {}

    #   Get all from table past_memberships
    if request.method == 'GET':
        construct = {
            'success': True,
            'past_memberships': Past_Memberships.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST':

        #   Trying to get parameters from the POST method
        try:
            person_id = EmptyValues.EMPTY_INT if request.json['person_id'] == EmptyValues.EMPTY_STRING else request.json['person_id']
            start_date = EmptyValues.EMPTY_STRING if request.json['start_date'] == EmptyValues.EMPTY_STRING else request.json['start_date']
            end_date = EmptyValues.EMPTY_STRING if request.json['end_date'] == EmptyValues.EMPTY_STRING else request.json['end_date']
            party_name = EmptyValues.EMPTY_STRING if request.json['party_name'] == EmptyValues.EMPTY_STRING else request.json['party_name']
            coalition_name = EmptyValues.EMPTY_STRING if request.json['coalition_name'] == EmptyValues.EMPTY_STRING else request.json['coalition_name']
            role_name = EmptyValues.EMPTY_STRING if request.json['role_name'] == EmptyValues.EMPTY_STRING else request.json['role_name']

            #   Verifying REQUIRED values
            if person_id == EmptyValues.EMPTY_INT or party_name == EmptyValues.EMPTY_STRING or role_name == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for person_id, party_name and role_name.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                past_membership = Past_Memberships(
                    person_id=person_id,
                    start_date=date.fromisoformat(start_date),
                    end_date=date.fromisoformat(end_date),
                    party_name=party_name, coalition_name=coalition_name,
                    role_name=role_name
                )
                past_membership.save()
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

@app.route('/past-membership/<int:past_membership_id>', methods=['GET', 'PUT', 'DELETE'])
def pastMembershipId(past_membership_id):

    #   Trying to get the past_membership with person_id
    past_membership = Past_Memberships.query.filter_by(past_membership_id=past_membership_id).first()

    #   If theres no result from the above query
    if not past_membership:
        construct = {
            'success': False,
            'message': 'Theres no data for that past_membership_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'past_membership': {
                'id': past_membership.past_membership_id,
                'person_id': past_membership.person_id,
                'start_date': past_membership.start_date.strftime('%Y-%m-%d'),
                'end_date': past_membership.end_date.strftime('%Y-%m-%d'),
                'party_name': past_membership.party_name,
                'coalition_name': past_membership.coalition_name,
                'role_name': past_membership.role_name
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT':
        construct = {}

        #   Trying to get parameters from the PUT method
        try:
            person_id = EmptyValues.EMPTY_INT if request.json['person_id'] == EmptyValues.EMPTY_STRING else request.json['person_id']
            start_date = EmptyValues.EMPTY_STRING if request.json['start_date'] == EmptyValues.EMPTY_STRING else request.json['start_date']
            end_date = EmptyValues.EMPTY_STRING if request.json['end_date'] == EmptyValues.EMPTY_STRING else request.json['end_date']
            party_name = EmptyValues.EMPTY_STRING if request.json['party_name'] == EmptyValues.EMPTY_STRING else request.json['party_name']
            coalition_name = EmptyValues.EMPTY_STRING if request.json['coalition_name'] == EmptyValues.EMPTY_STRING else request.json['coalition_name']
            role_name = EmptyValues.EMPTY_STRING if request.json['role_name'] == EmptyValues.EMPTY_STRING else request.json['role_name']

            #   Verifying REQUIRED values
            if person_id == EmptyValues.EMPTY_INT or party_name == EmptyValues.EMPTY_STRING or role_name == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for person_id, party_name and role_name.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                past_membership.person_id = person_id
                past_membership.start_date = date.fromisoformat(start_date)
                past_membership.end_date = date.fromisoformat(end_date)
                past_membership.party_name = party_name
                past_membership.coalition_name = coalition_name
                past_membership.role_name = role_name
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
            past_membership.delete()
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
