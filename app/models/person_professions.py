from app import db

class Person_Profession(db.Model):
    __tablename__ = 'person_professions'
    __table_args__ = {'sqlite_autoincrement': True}

    person_profession_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    #person_id = db.Column(db.Integer, nullable=False)
    profession_id = db.Column(db.Integer, db.ForeignKey('profession.profession_id'), nullable=False)


    def __init__(self, person_id, profession_id):
        self.person_id = person_id
        self.profession_id = profession_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        person_professions = Person_Profession.query.all()
        result = []
        for person_profession in person_professions:
            obj = {
                'person_profession_id': person_profession.person_profession_id,
                'person_id': person_profession.person_id,
                'profession_id': person_profession.profession_id
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
