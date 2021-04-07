from flask import request, jsonify
from app import app
from app.models.area import *
from app.const import *

@app.route('/area', methods=['GET', 'POST'])
def area():

    construct = {}

    #   Get all from table area
    if request.method == 'GET':
        construct = {
            'success': True,
            'areas': Area.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST':

        #   Trying to get parameters from the POST method
        try:
            ocd_id = EmptyValues.EMPTY_STRING if request.json['ocd_id'] == EmptyValues.EMPTY_STRING else request.json['ocd_id']
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            country = EmptyValues.EMPTY_STRING if request.json['country'] == EmptyValues.EMPTY_STRING else request.json['country']
            state = EmptyValues.EMPTY_STRING if request.json['state'] == EmptyValues.EMPTY_STRING else request.json['state']
            city = EmptyValues.EMPTY_STRING if request.json['city'] == EmptyValues.EMPTY_STRING else request.json['city']
            district_type = EmptyValues.EMPTY_INT if request.json['district_type'] == EmptyValues.EMPTY_STRING else request.json['district_type']
            parent_area_id = EmptyValues.EMPTY_INT if request.json['parent_area_id'] == EmptyValues.EMPTY_STRING else request.json['parent_area_id']

            #   Verifying REQUIRED values
            if ocd_id == EmptyValues.EMPTY_STRING or name == EmptyValues.EMPTY_STRING or country == EmptyValues.EMPTY_STRING or district_type == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for ocd_id, name, country and district_type.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                area = Area(
                    ocd_id=ocd_id, name=name, country=country, state=state,
                    city=city, district_type=district_type,
                    parent_area_id=parent_area_id
                )
                area.save()
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

@app.route('/area/<int:area_id>', methods=['GET', 'PUT', 'DELETE'])
def areaId(area_id):

    #   Trying to get the area with area_id
    area = Area.query.filter_by(area_id=area_id).first()

    #   If theres no result from the above query
    if not area:
        construct = {
            'success': False,
            'message': 'Theres no data for that area_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'area': {
                'area_id': area.area_id,
                'ocd_id': area.ocd_id,
                'name': {
                    'es_MX': area.name
                },
                'country': area.country,
                'state': area.state,
                'city': area.city,
                'district_type': Catalogues.DISTRICT_TYPES[area.district_type],
                'parent_area_id': "" if area.parent_area_id == EmptyValues.EMPTY_INT else area.parent_area_id
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT':
        construct = {}

        #   Trying to get parameters from the PUT method
        try:
            ocd_id = EmptyValues.EMPTY_STRING if request.json['ocd_id'] == EmptyValues.EMPTY_STRING else request.json['ocd_id']
            name = EmptyValues.EMPTY_STRING if request.json['name'] == EmptyValues.EMPTY_STRING else request.json['name']
            country = EmptyValues.EMPTY_STRING if request.json['country'] == EmptyValues.EMPTY_STRING else request.json['country']
            state = EmptyValues.EMPTY_STRING if request.json['state'] == EmptyValues.EMPTY_STRING else request.json['state']
            city = EmptyValues.EMPTY_STRING if request.json['city'] == EmptyValues.EMPTY_STRING else request.json['city']
            district_type = EmptyValues.EMPTY_INT if request.json['district_type'] == EmptyValues.EMPTY_STRING else request.json['district_type']
            parent_area_id = EmptyValues.EMPTY_INT if request.json['parent_area_id'] == EmptyValues.EMPTY_STRING else request.json['parent_area_id']

            #   Verifying REQUIRED values
            if ocd_id == EmptyValues.EMPTY_STRING or name == EmptyValues.EMPTY_STRING or country == EmptyValues.EMPTY_STRING or district_type == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for ocd_id, name, country and district_type.'
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                area.ocd_id = ocd_id
                area.name = name
                area.country = country
                area.state = state
                area.city = city
                area.district_type = district_type
                area.parent_area_id = parent_area_id
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
            area.delete()
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
