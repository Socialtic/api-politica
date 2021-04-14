from app import db
from app.const import OtherNames
from datetime import date
from app.controllers.other_names import *
from app.controllers.professions import *
from app.controllers.person_professions import *
from app.controllers.url import *

class Person(db.Model):
    __tablename__ = 'person'
    __table_args__ = {'sqlite_autoincrement': True}

    person_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    date_birth = db.Column(db.Date)
    gender_id = db.Column(db.Integer, nullable=False)
    dead_or_alive = db.Column(db.Boolean, nullable=False)
    last_degree_of_studies_id = db.Column(db.Integer)
    #contest_id = db.Column(db.Integer, db.ForeignKey('contest.contest_id'), nullable=True)
    contest_id = db.Column(db.Integer, nullable=True)

    def __init__(self, first_name, last_name, full_name, date_birth, gender_id, dead_or_alive, last_degree_of_studies_id, contest_id):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.date_birth = date_birth
        self.gender_id = gender_id
        self.dead_or_alive = dead_or_alive
        self.last_degree_of_studies_id = last_degree_of_studies_id
        self.contest_id = contest_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        persons = Person.query.all()
        result = []

        for person in persons:

            #   Getting other_names
            other_names_preferred = Other_Names.query.filter_by(other_name_type_id=OtherNames.PREFERRED, person_id=person.person_id)
            other_names_nickname = Other_Names.query.filter_by(other_name_type_id=OtherNames.NICKNAME, person_id=person.person_id)
            other_names_ballot_name = Other_Names.query.filter_by(other_name_type_id=OtherNames.BALLOT_NAME, person_id=person.person_id)

            other_names_preferred_val = []
            other_names_nickname_val = []
            other_names_ballot_name_val = []

            for other_name_preferred in other_names_preferred:
                other_name = {
                    'en_US': other_name_preferred.name
                }
                other_names_preferred_val.append(other_name)
                other_name = {
                    'es_MX': other_name_preferred.name
                }
                other_names_preferred_val.append(other_name)

            for other_name_nickname in other_names_nickname:
                other_name = {
                    'en_US': other_name_nickname.name
                }
                other_names_nickname_val.append(other_name)
                other_name = {
                    'es_MX': other_name_nickname.name
                }
                other_names_nickname_val.append(other_name)

            for other_name_ballot_name in other_names_ballot_name:
                other_name = {
                    'en_US': other_name_ballot_name.name
                }
                other_names_ballot_name_val.append(other_name)
                other_name = {
                    'es_MX': other_name_ballot_name.name
                }
                other_names_ballot_name_val.append(other_name)

            other_names = dict(preferred_name=other_names_preferred_val, nickname=other_names_nickname_val,ballot_name=other_names_ballot_name_val)

            #   Getting professions
            professions_val = []
            person_professions = Person_Profession.query.filter_by(person_id=person.person_id)
            for person_profession in person_professions:
                professions = Profession.query.filter_by(profession_id=person_profession.profession_id)
                for profession in professions:
                    professions_val.append(profession.description)

            obj = {
                'id': person.person_id,
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
                'date_birth': "" if person.date_birth.strftime('%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else person.date_birth.strftime('%Y-%m-%d'),
                'gender': Catalogues.GENDERS[person.gender_id],
                'dead_or_alive': person.dead_or_alive,
                'last_degree_of_studies': "" if person.last_degree_of_studies_id == EmptyValues.EMPTY_INT else Catalogues.DEGREES_OF_STUDIES[person.last_degree_of_studies_id],
                'contest_id': "" if person.contest_id == EmptyValues.EMPTY_INT else person.contest_id,
                'other_names': other_names,
                'professions': professions_val,
                'fb_urls': Url.get_person_fb_urls(person.person_id),
                'ig_urls': Url.get_person_ig_urls(person.person_id),
                'websites': Url.get_party_or_coalition_or_person_websites_urls(person.person_id, URL_OWNER_TYPE.PERSON),
                'photo_urls': Url.get_person_photo_urls(person.person_id),
                'social_network_accounts': Url.get_person_social_networks_urls(person.person_id)
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
