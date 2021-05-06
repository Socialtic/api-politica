from app import db
from typing import List
from datetime import date

from app.const import Catalogues, EmptyValues, URL_OWNER_TYPE, OtherNames

from app.models.person_professions import PersonProfessionModel
from app.models.professions import ProfessionModel
from app.models.url import UrlModel
from app.models.other_names import OtherNamesModel

class PersonModel(db.Model):
    __tablename__ = 'person'
    __table_args__ = {'sqlite_autoincrement': True}

    person_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    date_birth = db.Column(db.Date)
    gender = db.Column(db.Integer, nullable=False) #gender_ir
    dead_or_alive = db.Column(db.Boolean, nullable=False)
    last_degree_of_studies = db.Column(db.Integer) #last_degree_of_studies_id
    contest_id = db.Column(db.Integer, db.ForeignKey('contest.contest_id'), nullable=True)
    #contest_id = db.Column(db.Integer, nullable=True)

    def __init__(self, first_name, last_name, full_name, date_birth, gender, dead_or_alive, last_degree_of_studies, contest_id):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.date_birth = date_birth
        self.gender = gender
        self.dead_or_alive = dead_or_alive
        self.last_degree_of_studies = last_degree_of_studies
        self.contest_id = contest_id

    def json(self):
        #   Getting other_names
        other_names_preferred = OtherNamesModel.query.filter_by(other_name_type=OtherNames.PREFERRED, person_id=self.person_id)
        other_names_nickname = OtherNamesModel.query.filter_by(other_name_type=OtherNames.NICKNAME, person_id=self.person_id)
        other_names_ballot_name = OtherNamesModel.query.filter_by(other_name_type=OtherNames.BALLOT_NAME, person_id=self.person_id)

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

        other_names = dict(preferred_name=other_names_preferred_val, nickname=other_names_nickname_val,
                           ballot_name=other_names_ballot_name_val)

        #   Getting professions
        professions_val = []
        person_professions = PersonProfessionModel.query.filter_by(person_id=self.person_id)
        for person_profession in person_professions:
            professions = ProfessionModel.query.filter_by(profession_id=person_profession.profession_id)
            for profession in professions:
                professions_val.append(profession.description)

        obj = {
            'id': self.person_id,
            'first_name': {
                'en_US': self.first_name,
                'es_MX': self.first_name
            },
            'last_name': {
                'en_US': self.last_name,
                'es_MX': self.last_name
            },
            'full_name': {
                'en_US': self.full_name,
                'es_MX': self.full_name
            },
            'date_birth': "" if self.date_birth.strftime('%Y-%m-%d') == date.fromisoformat(
                EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else self.date_birth.strftime('%Y-%m-%d'),
            'gender': Catalogues.GENDERS[self.gender],
            'dead_or_alive': self.dead_or_alive,
            'last_degree_of_studies': "" if self.last_degree_of_studies == EmptyValues.EMPTY_INT else
            Catalogues.DEGREES_OF_STUDIES[self.last_degree_of_studies],
            'contest_id': "" if self.contest_id == EmptyValues.EMPTY_INT else self.contest_id,
            'other_names': other_names,
            'professions': professions_val,
            'fb_urls': UrlModel.get_person_fb_urls(self.person_id),
            'ig_urls': UrlModel.get_person_ig_urls(self.person_id),
            'websites': UrlModel.get_party_or_coalition_or_person_websites_urls(self.person_id, URL_OWNER_TYPE.PERSON),
            'photo_urls': UrlModel.get_person_photo_urls(self.person_id),
            'social_network_accounts': UrlModel.get_person_social_networks_urls(self.person_id)
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "PersonModel":
        return cls.query.filter_by(person_id=_id).first()

    @classmethod
    def find_all(cls) -> List["PersonModel"]:
        query_all = cls.query.all()
        result = []
        for one_element in query_all:
            result.append(one_element.json())
        return result

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
