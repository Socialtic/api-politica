from flask import request, jsonify
from app import application as app
from app.const import *
from app.models.contest import *
from app.models.role import *
from app.models.person import *
from app import isOnDev

@app.route('/contest', methods=['GET', 'POST'])
def contest_fun():

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Get all from table contest
    if request.method == 'GET':
        construct = {
            'success': True,
            'contests': Contest.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST' and isOnDev:

        #   Trying to get parameters from the POST method
        try:
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
            title = EmptyValues.EMPTY_STRING if request.json['title'] == EmptyValues.EMPTY_STRING else request.json['title']
            membership_id_winner = EmptyValues.EMPTY_INT if request.json['membership_id_winner'] == EmptyValues.EMPTY_STRING else request.json['membership_id_winner']
            start_date = EmptyValues.EMPTY_DATE if request.json['start_date'] == EmptyValues.EMPTY_STRING else request.json['start_date']
            end_date = EmptyValues.EMPTY_DATE if request.json['end_date'] == EmptyValues.EMPTY_STRING else request.json['end_date']
            election_identifier = EmptyValues.EMPTY_STRING if request.json['election_identifier'] == EmptyValues.EMPTY_STRING else request.json['election_identifier']

            #   Verifying REQUIRED values
            if area_id == EmptyValues.EMPTY_INT or title == EmptyValues.EMPTY_STRING or election_identifier == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for area_id, title and election_identifier.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                contest = Contest(
                    area_id=area_id, title=title, membership_id_winner=membership_id_winner,
                    start_date=date.fromisoformat(start_date), end_date=date.fromisoformat(end_date),
                    election_identifier=election_identifier
                )
                contest.save()
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

@app.route('/contest/<int:contest_id>', methods=['GET', 'PUT', 'DELETE'])
def contestId(contest_id):

    construct = {
        'success': False,
        'message': 'Method not allowed :)'
    }
    response = jsonify(construct)
    response.status_code = HttpStatus.NOT_ALLOWED

    #   Trying to get the area with area_id
    contest = Contest.query.filter_by(contest_id=contest_id).first()

    #   If theres no result from the above query
    if not contest:
        construct = {
            'success': False,
            'message': 'Theres no data for that contest_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':

        roles = Role.query.filter_by(contest_id=contest.contest_id)
        persons = Person.query.filter_by(contest_id=contest.contest_id)

        role_ids = []
        person_ids = []

        for role in roles:
            role_ids.append(role.role_id)

        for person in persons:
            person_ids.append(person.person_id)

        construct = {
            'success': True,
            'contest': {
                'id': contest.contest_id,
                'area_id': contest.area_id,
                'title': {
                    'en_US': contest.title,
                },
                'membership_id_winner': '' if contest.membership_id_winner == EmptyValues.EMPTY_INT else contest.membership_id_winner,
                'start_date': '' if contest.start_date.strftime('%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else contest.start_date.strftime('%Y-%m-%d'),
                'end_date': '' if contest.end_date.strftime('%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else contest.end_date.strftime('%Y-%m-%d'),
                'election_identifier': contest.election_identifier,
                'role_ids': role_ids,
                'person_ids': person_ids
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT' and isOnDev:
        construct = {}

        #   Trying to get parameters from the PUT method
        try:
            area_id = EmptyValues.EMPTY_INT if request.json['area_id'] == EmptyValues.EMPTY_STRING else request.json['area_id']
            title = EmptyValues.EMPTY_STRING if request.json['title'] == EmptyValues.EMPTY_STRING else request.json['title']
            membership_id_winner = EmptyValues.EMPTY_INT if request.json['membership_id_winner'] == EmptyValues.EMPTY_STRING else request.json['membership_id_winner']
            start_date = EmptyValues.EMPTY_DATE if request.json['start_date'] == EmptyValues.EMPTY_STRING else request.json['start_date']
            end_date = EmptyValues.EMPTY_DATE if request.json['end_date'] == EmptyValues.EMPTY_STRING else request.json['end_date']
            election_identifier = EmptyValues.EMPTY_STRING if request.json['election_identifier'] == EmptyValues.EMPTY_STRING else request.json['election_identifier']

            #   Verifying REQUIRED values
            if area_id == EmptyValues.EMPTY_INT or title == EmptyValues.EMPTY_STRING or election_identifier == EmptyValues.EMPTY_STRING:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for area_id, title and election_identifier.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                contest.area_id= area_id
                contest.title = title
                contest.membership_id_winner = membership_id_winner
                contest.start_date = date.fromisoformat(start_date)
                contest.end_date = date.fromisoformat(end_date)
                contest.election_identifier = election_identifier
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
            contest.delete()
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
