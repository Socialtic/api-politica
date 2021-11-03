from app import db

class PersonProfessionModel(db.Model):
    __tablename__ = 'person_professions'
    __table_args__ = {'sqlite_autoincrement': True}

    person_profession_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    #person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    person_id = db.Column(db.Integer, nullable=False)
    #profession_id = db.Column(db.Integer, db.ForeignKey('profession.profession_id'), nullable=False)
    profession_id = db.Column(db.Integer, nullable=False)

    def __init__(self, person_id, profession_id):
        self.person_id = person_id
        self.profession_id = profession_id

    def json(self):
        obj = {
            'id': self.person_profession_id,
            'person_id': "ar-" + str(self.person_id),
            'profession_id': self.profession_id
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "PersonProfessionModel":
        return cls.query.filter_by(person_profession_id=_id).first()

    @classmethod
    def find_all(cls):
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
