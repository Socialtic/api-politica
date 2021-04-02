from app import db
from app.const import Catalogues

class Person_Professions(db.Model):
    __tablename__ = 'person_professions'
    __table_args__ = {'sqlite_autoincrement': True}

    person_profession_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    #person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    person_id = db.Column(db.Integer, nullable=False)
    profession_id = db.Column(db.Integer, nullable=False)


    def __init__(self, person_id, profession_id):
        self.person_id = person_id
        self.profession_id = profession_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        professions = Person_Professions.query.all()
        result = []
        for profession in professions:
            obj = {
                'person_profession_id': profession.person_profession_id,
                'person_id': profession.person_id,
                'profession': Catalogues.PROFESSIONS[profession.profession_id]
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
