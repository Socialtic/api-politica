from app import db
from typing import List
from app.const import Catalogues

class OtherNamesModel(db.Model):
    __tablename__ = 'other_names'
    __table_args__ = {'sqlite_autoincrement': True}

    other_name_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    other_name_type = db.Column(db.Integer, nullable=False) #other_name_type_id
    name = db.Column(db.String(50), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    #person_id = db.Column(db.Integer, nullable=False)

    def __init__(self, other_name_type, name, person_id):
        self.other_name_type = other_name_type
        self.name = name
        self.person_id = person_id

    def json(self):
        obj = {
            'id': self.other_name_id,
            'other_name_type': Catalogues.OTHER_NAMES_TYPES[self.other_name_type],
            'name': self.name,
            'person_id': self.person_id
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "OtherNamesModel":
        return cls.query.filter_by(other_name_id=_id).first()

    @classmethod
    def find_all(cls) -> List["OtherNamesModel"]:
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
