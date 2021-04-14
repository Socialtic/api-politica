from flask import request, jsonify
from app import application as app
from app.models.memberships import *
from app.const import *
from datetime import date

@app.route('/membership', methods=['GET', 'POST'])
def Memberships():

    construct = {}

    #   Get all from table memberships
    if request.method == 'GET':
        construct = {
            'success': True,
            'memberships': Membership.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    #   Trying to insert into the table
    elif request.method == 'POST':

        #   Trying to get parameters from the POST method
        try:
            person_id = EmptyValues.EMPTY_INT if request.json['person_id'] == EmptyValues.EMPTY_STRING else request.json['person_id']
            role_id = EmptyValues.EMPTY_INT if request.json['role_id'] == EmptyValues.EMPTY_STRING else request.json['role_id']
            party_id = EmptyValues.EMPTY_INT if request.json['party_id'] == EmptyValues.EMPTY_STRING else request.json['party_id']
            coalition_id = EmptyValues.EMPTY_INT if request.json['coalition_id'] == EmptyValues.EMPTY_STRING else request.json['coalition_id']
            contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']
            goes_for_coalition = EmptyValues.EMPTY_INT if request.json['goes_for_coalition'] == EmptyValues.EMPTY_STRING else request.json['goes_for_coalition']
            membership_type = EmptyValues.EMPTY_INT if request.json['membership_type'] == EmptyValues.EMPTY_STRING else request.json['membership_type']
            goes_for_reelection = EmptyValues.EMPTY_INT if request.json['goes_for_reelection'] == EmptyValues.EMPTY_STRING else request.json['goes_for_reelection']
            start_date = EmptyValues.EMPTY_DATE if request.json['start_date'] == EmptyValues.EMPTY_STRING else request.json['start_date']
            end_date = EmptyValues.EMPTY_DATE if request.json['end_date'] == EmptyValues.EMPTY_STRING else request.json['end_date']
            is_substitute = EmptyValues.EMPTY_INT if request.json['is_substitute'] == EmptyValues.EMPTY_STRING else request.json['is_substitute']
            parent_membership_id = EmptyValues.EMPTY_INT if request.json['parent_membership_id'] == EmptyValues.EMPTY_STRING else request.json['parent_membership_id']
            changed_from_substitute = EmptyValues.EMPTY_INT if request.json['changed_from_substitute'] == EmptyValues.EMPTY_STRING else request.json['changed_from_substitute']
            date_changed_from_substitute = EmptyValues.EMPTY_DATE if request.json['date_changed_from_substitute'] == EmptyValues.EMPTY_STRING else request.json['date_changed_from_substitute']

            #   Verifying REQUIRED values
            if person_id == EmptyValues.EMPTY_INT or role_id == EmptyValues.EMPTY_INT \
                    or party_id == EmptyValues.EMPTY_INT \
                    or goes_for_coalition == EmptyValues.EMPTY_INT or membership_type == EmptyValues.EMPTY_INT \
                    or goes_for_reelection == EmptyValues.EMPTY_INT or is_substitute == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for person_id, role_id, party_id, ' \
                                     'goes_for_coalition, membership_type, goes_for_coalition and is_substitute. '
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to INSERT into the DB
            try:
                membership = Membership(
                    person_id=person_id, role_id=role_id, party_id=party_id, coalition_id=coalition_id,
                    contest_id=contest_id, goes_for_coalition=goes_for_coalition, membership_type=membership_type,
                    goes_for_reelection=goes_for_reelection,
                    start_date=date.fromisoformat(start_date), end_date=date.fromisoformat(end_date),
                    is_substitute=is_substitute, parent_membership_id=parent_membership_id,
                    changed_from_substitute=changed_from_substitute,
                    date_changed_from_substitute=date.fromisoformat(date_changed_from_substitute)
                )
                membership.save()
                construct['success'] = True
                construct['message'] = 'Data saved'
                response = jsonify(construct)
                response.status_code = HttpStatus.CREATED

            #   Failing while INSERTING into the DB
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

@app.route('/membership/<int:membership_id>', methods=['GET', 'PUT', 'DELETE'])
def membershipId(membership_id):

    #   Trying to get the past_membership with membership_id
    membership = Membership.query.filter_by(membership_id=membership_id).first()

    #   If theres no result from the above query
    if not membership:
        construct = {
            'success': False,
            'message': 'Theres no data for that membership_id'
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
        return response

    #   If theres a result, then ...
    #   Get their data
    if request.method == 'GET':
        construct = {
            'success': True,
            'membership': {
                'id': membership.membership_id,
                'person_id': membership.person_id,
                'role_id': membership.role_id,
                'party_ids': [membership.party_id],
                'contest_id': "" if membership.contest_id == EmptyValues.EMPTY_INT else membership.contest_id,
                'coalition_id': "" if membership.coalition_id == EmptyValues.EMPTY_INT else membership.coalition_id,
                'goes_for_coalition': membership.goes_for_coalition,
                'membership_type': Catalogues.MEMBERSHIP_TYPES[membership.membership_type],
                'goes_for_reelection': membership.goes_for_reelection,
                'start_date': "" if membership.start_date.strftime('%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else membership.start_date.strftime('%Y-%m-%d'),
                'end_date': "" if membership.end_date.strftime('%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else membership.end_date.strftime('%Y-%m-%d'),
                'is_substitute': membership.is_substitute,
                'parent_membership_id': "" if membership.parent_membership_id == EmptyValues.EMPTY_INT else membership.parent_membership_id,
                'changed_from_substitute': "" if membership.changed_from_substitute == EmptyValues.EMPTY_INT else membership.changed_from_substitute,
                'date_changed_from_substitute': "" if membership.date_changed_from_substitute.strftime('%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else membership.date_changed_from_substitute.strftime('%Y-%m-%d'),
                'source_urls': Url.get_membership_source_urls(membership.membership_id)
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
            role_id = EmptyValues.EMPTY_INT if request.json['role_id'] == EmptyValues.EMPTY_STRING else request.json['role_id']
            party_id = EmptyValues.EMPTY_INT if request.json['party_id'] == EmptyValues.EMPTY_STRING else request.json['party_id']
            coalition_id = EmptyValues.EMPTY_INT if request.json['coalition_id'] == EmptyValues.EMPTY_STRING else request.json['coalition_id']
            contest_id = EmptyValues.EMPTY_INT if request.json['contest_id'] == EmptyValues.EMPTY_STRING else request.json['contest_id']
            goes_for_coalition = EmptyValues.EMPTY_INT if request.json['goes_for_coalition'] == EmptyValues.EMPTY_STRING else request.json['goes_for_coalition']
            membership_type = EmptyValues.EMPTY_INT if request.json['membership_type'] == EmptyValues.EMPTY_STRING else request.json['membership_type']
            goes_for_reelection = EmptyValues.EMPTY_INT if request.json['goes_for_reelection'] == EmptyValues.EMPTY_STRING else request.json['goes_for_reelection']
            start_date = EmptyValues.EMPTY_DATE if request.json['start_date'] == EmptyValues.EMPTY_STRING else request.json['start_date']
            end_date = EmptyValues.EMPTY_DATE if request.json['end_date'] == EmptyValues.EMPTY_STRING else request.json['end_date']
            is_substitute = EmptyValues.EMPTY_INT if request.json['is_substitute'] == EmptyValues.EMPTY_STRING else request.json['is_substitute']
            parent_membership_id = EmptyValues.EMPTY_INT if request.json['parent_membership_id'] == EmptyValues.EMPTY_STRING else request.json['parent_membership_id']
            changed_from_substitute = EmptyValues.EMPTY_INT if request.json['changed_from_substitute'] == EmptyValues.EMPTY_STRING else request.json['changed_from_substitute']
            date_changed_from_substitute = EmptyValues.EMPTY_DATE if request.json['date_changed_from_substitute'] == EmptyValues.EMPTY_STRING else request.json['date_changed_from_substitute']

            #   Verifying REQUIRED values
            if person_id == EmptyValues.EMPTY_INT or role_id == EmptyValues.EMPTY_INT \
                    or party_id == EmptyValues.EMPTY_INT \
                    or goes_for_coalition == EmptyValues.EMPTY_INT or membership_type == EmptyValues.EMPTY_INT \
                    or goes_for_reelection == EmptyValues.EMPTY_INT or is_substitute == EmptyValues.EMPTY_INT:
                construct['success'] = False
                construct['error'] = 'Missing data. Required values for person_id, role_id, party_id, ' \
                                     'goes_for_coalition, membership_type, goes_for_coalition and is_substitute. '
                response = jsonify(construct)
                response.status_code = HttpStatus.BAD_REQUEST
                return response

            #   Trying to UPDATE into the DB
            try:
                membership.person_id = person_id
                membership.role_id = role_id
                membership.party_id = party_id
                membership.contest_id = contest_id
                membership.coalition_id = coalition_id
                membership.goes_for_coalition = goes_for_coalition
                membership.membership_type = membership_type
                membership.goes_for_reelection = goes_for_reelection
                membership.start_date = date.fromisoformat(start_date)
                membership.end_date = date.fromisoformat(end_date)
                membership.is_substitute = is_substitute
                membership.parent_membership_id = parent_membership_id
                membership.changed_from_substitute = changed_from_substitute
                membership.date_changed_from_substitute = date.fromisoformat(date_changed_from_substitute)
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
            membership.delete()
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
