from flask import request, jsonify
from app import app
from app.models.other_names import *
from app.models.person_professions import *
from app.models.person import *
from app.const import *
from datetime import date

@app.route('/person', methods=['GET', 'POST'])
def person():

    construct = {}

    #   Get all from table person
    if request.method == 'GET':
        construct = {
            'success': True,
            'persons': Person.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST':

        #   Trying to get parameters from the POST method
        try:
            first_name = EmptyValues.EMPTY_STRING if request.json['first_name'] == EmptyValues.EMPTY_STRING else request.json['first_name']
            last_name = EmptyValues.EMPTY_STRING if request.json['last_name'] == EmptyValues.EMPTY_STRING else request.json['last_name']
            full_name = EmptyValues.EMPTY_STRING if request.json['full_name'] == EmptyValues.EMPTY_STRING else request.json['full_name']
            date_birth = EmptyValues.EMPTY_STRING if request.json['date_birth'] == EmptyValues.EMPTY_STRING else request.json['date_birth']
            gender = EmptyValues.EMPTY_INT if request.json['gender'] == EmptyValues.EMPTY_STRING else request.json['gender']
            dead_or_alive = EmptyValues.EMPTY_INT if request.json['dead_or_alive'] == EmptyValues.EMPTY_STRING else request.json['dead_or_alive']
            last_degree_of_studies = EmptyValues.EMPTY_INT if request.json['last_degree_of_studies'] == EmptyValues.EMPTY_STRING else request.json['last_degree_of_studies']
            contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']

            #   Verifying REQUIRED values
            if first_name == EmptyValues.EMPTY_STRING or last_name == EmptyValues.EMPTY_STRING or full_name == EmptyValues.EMPTY_STRING or gender == EmptyValues.EMPTY_INT or dead_or_alive == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for first_name, last_name, full_name, gender and dead_or_alive.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                person = Person(
                    first_name=first_name, last_name=last_name, full_name=full_name,
                    date_birth=date.fromisoformat(date_birth), gender_id=gender, dead_or_alive=dead_or_alive,
                    last_degree_of_studies_id=last_degree_of_studies, contest_id=contest_id
                )
                person.save()
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

@app.route('/person/<int:person_id>', methods=['GET', 'PUT', 'DELETE'])
def personId(person_id):

    #   Trying to get the area with person_id
    person = Person.query.filter_by(person_id=person_id).first()

    #   If theres no result from the above query
    if not person:
        construct = {
            'success': False,
            'message': 'Theres no data for that person_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'person': {
                'person_id': person.person_id,
                'first_name': {
                    'en_US': person.first_name,
                    'es_MX': person.first_name
                },
                'last_name': {
                    'en_US': person.last_name,
                    'es_MX': person.last_name
                },
                'full_name': {
                    'en_US': person.full_name,
                    'es_MX': person.full_name
                },
                'date_birth': person.date_birth.strftime('%Y-%m-%d'),
                'gender': Catalogues.GENDERS[person.gender_id],
                'dead_or_alive': person.dead_or_alive,
                'last_degree_of_studies': Catalogues.DEGREES_OF_STUDIES[person.last_degree_of_studies_id],
                'contest_id': person.contest_id
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT':
        construct = {}

        #   Trying to get parameters from the PUT method
        try:
            first_name = EmptyValues.EMPTY_STRING if request.json['first_name'] == EmptyValues.EMPTY_STRING else request.json['first_name']
            last_name = EmptyValues.EMPTY_STRING if request.json['last_name'] == EmptyValues.EMPTY_STRING else request.json['last_name']
            full_name = EmptyValues.EMPTY_STRING if request.json['full_name'] == EmptyValues.EMPTY_STRING else request.json['full_name']
            date_birth = EmptyValues.EMPTY_STRING if request.json['date_birth'] == EmptyValues.EMPTY_STRING else request.json['date_birth']
            gender = EmptyValues.EMPTY_INT if request.json['gender'] == EmptyValues.EMPTY_STRING else request.json['gender']
            dead_or_alive = EmptyValues.EMPTY_INT if request.json['dead_or_alive'] == EmptyValues.EMPTY_STRING else request.json['dead_or_alive']
            last_degree_of_studies = EmptyValues.EMPTY_INT if request.json['last_degree_of_studies'] == EmptyValues.EMPTY_STRING else request.json['last_degree_of_studies']
            contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']

            #   Verifying REQUIRED values
            if first_name == EmptyValues.EMPTY_STRING or last_name == EmptyValues.EMPTY_STRING or full_name == EmptyValues.EMPTY_STRING or gender == EmptyValues.EMPTY_INT or dead_or_alive == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for first_name, last_name, full_name, gender and dead_or_alive.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                person.first_name = first_name
                person.last_name = last_name
                person.full_name = full_name
                person.date_birth = date.fromisoformat(date_birth)
                person.gender_id = gender
                person.dead_or_alive = dead_or_alive
                person.last_degree_of_studies_id = last_degree_of_studies
                person.contest_id = contest_id
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
            person.delete()
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
