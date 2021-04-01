from flask import request, jsonify
from app import app
from app.models.area import *
from app.const import HttpStatus

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
            ocd_id = "" if request.json['ocd_id'] == "" else request.json['ocd_id']
            name = "" if request.json['name'] == "" else request.json['name']
            country = "" if request.json['country'] == "" else request.json['country']
            state = "" if request.json['state'] == "" else request.json['state']
            city = "" if request.json['city'] == "" else request.json['city']
            distric_type = "" if request.json['distric_type'] == "" else request.json['distric_type']
            parent_area_id = (-1) if request.json['parent_area_id'] == "" else request.json['parent_area_id']

            #   Verifying REQUIRED values
            if ocd_id == "" or name == "" or country == "" or distric_type == "":
                construct['success'] = False
                construct['error'] = "Missing data. Required values for ocd_id, name, country and distric_type."
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                area = Area(
                    ocd_id=ocd_id, name=name, country=country, state=state,
                    city=city, distric_type=distric_type,
                    parent_area_id=parent_area_id
                )
                area.save()
                construct['success'] = True
                construct['message'] = 'Data saved'
                response = jsonify(construct)
                response.status_code = HttpStatus.CREATED
            #   Failling while INSERTING into the DB
            except Exception as e:
                construct['success'] = False
                construct['error'] = str(e)
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
        #   Missing parameters from the POST method
        except Exception as e:
            construct['success'] = False
            construct['error'] = "Missing data. Missing value " + str(e)
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
            'message': "Theres no data for that area_id"
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
                'name': area.name,
                'country': area.country,
                'state': area.state,
                'city': area.city,
                'distric_type': area.distric_type,
                'parent_area_id': area.parent_area_id
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Update their data
    elif request.method == 'PUT':
        construct = {}
        #   Trying to get parameters from the PUT method
        try:
            ocd_id = "" if request.json['ocd_id'] == "" else request.json['ocd_id']
            name = "" if request.json['name'] == "" else request.json['name']
            country = "" if request.json['country'] == "" else request.json['country']
            state = "" if request.json['state'] == "" else request.json['state']
            city = "" if request.json['city'] == "" else request.json['city']
            distric_type = "" if request.json['distric_type'] == "" else request.json['distric_type']
            parent_area_id = (-1) if request.json['parent_area_id'] == "" else request.json['parent_area_id']

            #   Verifying REQUIRED values
            if ocd_id == "" or name == "" or country == "" or distric_type == "":
                construct['success'] = False
                construct['error'] = "Missing data. Required values for ocd_id, name, country and distric_type."
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
                area.distric_type = distric_type
                area.parent_area_id = parent_area_id
                db.session.commit()
                construct['success'] = True
                construct['message'] = 'Data saved'
                response = jsonify(construct)
                response.status_code = HttpStatus.CREATED
            #   Failling while UPDATING into the DB
            except Exception as e:
                construct['success'] = False
                construct['error'] = str(e)
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
        #   Missing parameters from the PUT method
        except Exception as e:
            construct['success'] = False
            construct['error'] = "Missing data. Missing value " + str(e)
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
