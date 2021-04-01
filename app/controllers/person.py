from flask import request, jsonify
from app import app
from app.models.person import *
from app.const import HttpStatus

@app.route('/person', methods=['GET', 'POST'])
def person():
    if request.method == 'GET':
        construct = {
            'error': [],
            'success': True,
            'persons': Person.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    elif request.method == 'POST':
        name = None if request.json['name'] is "" else request.json['name']
        construct = {}
        try:
            person = Person(name=name)
            person.save()
            construct['success'] = True
            construct['message'] = 'Data saved'
            response = jsonify(construct)
            response.status_code = HttpStatus.CREATED
            print("<name: {}>".format(name))
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
    return response

@app.route('/person/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def personId(id):
    person = Person.query.filter_by(id=id).first()
    if request.method == 'GET':
        construct = {
            'error': [],
            'success': True,
            'person': {
                'id': person.id,
                'name': person.name
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
    elif request.method == 'PUT':
        name = None if request.json['name'] is "" else request.json['name']
        construct = {}
        try:
            person.name = name
            db.session.commit()
            construct['success'] = True
            construct['message'] = 'Data saved'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
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
