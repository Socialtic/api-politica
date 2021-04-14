from app import db
from app.const import Catalogues

class Other_Names(db.Model):
    __tablename__ = 'other_names'
    __table_args__ = {'sqlite_autoincrement': True}

    other_name_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    other_name_type_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    #person_id = db.Column(db.Integer, nullable=False)

    def __init__(self, other_name_type_id, name, person_id):
        self.other_name_type_id = other_name_type_id
        self.name = name
        self.person_id = person_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        other_names = Other_Names.query.all()
        result = []
        for other_name in other_names:
            obj = {
                'id': other_name.other_name_id,
                'other_name_type_id': Catalogues.OTHER_NAMES_TYPES[other_name.other_name_type_id],
                'name': other_name.name,
                'person_id': other_name.person_id
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
