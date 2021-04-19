from app import db
from app.models.role import *
from app.models.person import *
from app.const import EmptyValues

class Contest(db.Model):
    __tablename__ = 'contest'
    __table_args__ = {'sqlite_autoincrement': True}

    contest_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=True)
    title = db.Column(db.String(50), nullable=False)
    #membership_id_winner = db.Column(db.Integer, db.ForeignKey('membership.membership_id'), nullable=True)
    membership_id_winner = db.Column(db.Integer, nullable=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    election_identifier = db.Column(db.String(100), nullable=False)

    def __init__(self, area_id, title, membership_id_winner, start_date, end_date, election_identifier):
        self.area_id = area_id
        self.title = title
        self.membership_id_winner = membership_id_winner
        self.start_date = start_date
        self.end_date = end_date
        self.election_identifier = election_identifier

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        contests = Contest.query.all()
        result = []
        for contest in contests:

            roles = Role.query.filter_by(contest_id=contest.contest_id)
            persons = Person.query.filter_by(contest_id=contest.contest_id)

            role_ids = []
            person_ids = []

            for role in roles:
                role_ids.append(role.role_id)

            for person in persons:
                person_ids.append(person.person_id)

            obj = {
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
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
