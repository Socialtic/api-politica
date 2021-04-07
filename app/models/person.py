from app import db
from app.const import Catalogues

class Person(db.Model):
    __tablename__ = 'person'
    __table_args__ = {'sqlite_autoincrement': True}

    person_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, nullable=False)
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
            obj = {
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
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
