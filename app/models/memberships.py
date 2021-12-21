from app import db
from app.const import Catalogues, EmptyValues
from datetime import date
from app.models.url import UrlModel

class MembershipModel(db.Model):
    __tablename__ = 'membership'
    __table_args__ = {'sqlite_autoincrement': True}

    membership_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.role_id'), nullable=False)
    party_id = db.Column(db.Integer, db.ForeignKey('party.party_id'), nullable=False)
    #coalition_id = db.Column(db.Integer, db.ForeignKey('coalition.coalition_id'), nullable=True)
    coalition_id = db.Column(db.Integer, nullable=True)
    #contest_id = db.Column(db.Integer, db.ForeignKey('contest.contest_id'), nullable=True)
    contest_id = db.Column(db.Integer, nullable=True)
    goes_for_coalition = db.Column(db.Boolean, nullable=False)
    membership_type = db.Column(db.Integer, nullable=False)
    goes_for_reelection = db.Column(db.Boolean, nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    is_substitute = db.Column(db.Boolean, nullable=False)
    #parent_membership_id = db.Column(db.Integer, db.ForeignKey('membership.membership_id'), nullable=True)
    parent_membership_id = db.Column(db.Integer, nullable=True)
    changed_from_substitute = db.Column(db.Boolean)
    date_changed_from_substitute = db.Column(db.Date)


    def __init__(
            self, person_id, role_id, party_id, coalition_id, contest_id, goes_for_coalition,
            membership_type, goes_for_reelection, start_date, end_date, is_substitute,
            parent_membership_id, changed_from_substitute, date_changed_from_substitute
        ):
        self.person_id = person_id
        self.role_id = role_id
        self.party_id = party_id
        self.coalition_id = coalition_id
        self.contest_id = contest_id
        self.goes_for_coalition = goes_for_coalition
        self.membership_type = membership_type
        self.goes_for_reelection = goes_for_reelection
        self.start_date = start_date
        self.end_date = end_date
        self.is_substitute = is_substitute
        self.parent_membership_id = parent_membership_id
        self.changed_from_substitute = changed_from_substitute
        self.date_changed_from_substitute = date_changed_from_substitute

    def json(self):
        obj = {
            'id': self.membership_id,
            'person_id': "ar-" + str(self.person_id),
            'role_id': self.role_id,
            'party_ids': [self.party_id],
            'coalition_id': "" if self.coalition_id == EmptyValues.EMPTY_INT else self.coalition_id,
            'contest_id': "" if self.contest_id == EmptyValues.EMPTY_INT else self.contest_id,
            'goes_for_coalition': self.goes_for_coalition,
            'membership_type': Catalogues.MEMBERSHIP_TYPES[self.membership_type],
            'goes_for_reelection': self.goes_for_reelection,
            'start_date': "" if self.start_date.strftime('%Y-%m-%d') == date.fromisoformat(
                EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else self.start_date.strftime('%Y-%m-%d'),
            'end_date': "" if self.end_date.strftime('%Y-%m-%d') == date.fromisoformat(
                EmptyValues.EMPTY_DATE).strftime('%Y-%m-%d') else self.end_date.strftime('%Y-%m-%d'),
            'is_substitute': self.is_substitute,
            'parent_membership_id': "" if self.parent_membership_id == EmptyValues.EMPTY_INT else self.parent_membership_id,
            'changed_from_substitute': "" if self.changed_from_substitute == EmptyValues.EMPTY_INT else self.changed_from_substitute,
            'date_changed_from_substitute': "" if self.date_changed_from_substitute.strftime(
                '%Y-%m-%d') == date.fromisoformat(EmptyValues.EMPTY_DATE).strftime(
                '%Y-%m-%d') else self.date_changed_from_substitute.strftime('%Y-%m-%d'),
            'source_urls': UrlModel.get_membership_source_urls(self.membership_id)
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "MembershipModel":
        return cls.query.filter_by(membership_id=_id).first()

    @classmethod
    def find_all(cls):
        query_all = cls.query.all()
        result = []
        for one_element in query_all:
            result.append(one_element.json())
        return result

    @classmethod
    def find_officeholders(cls):
        query_all = cls.query.filter_by(membership_type=1).all()
        result = []
        for one_element in query_all:
            result.append(one_element.json())
        return result

    @classmethod
    def find_officeholders_persons_parties(cls):
        query_all = cls.query.filter_by(membership_type=1).all()
        persons = []
        parties = []
        for one_element in query_all:
            persons.append(one_element.person_id)
            parties.append(one_element.party_id)
        return sorted(persons), list(set(sorted(parties)))

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
