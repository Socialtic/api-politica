from app import db
from typing import List

class ChamberModel(db.Model):
    __tablename__ = 'chamber'
    __table_args__ = {'sqlite_autoincrement': True}

    chamber_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=False)

    def __init__(self, name, area_id):
        self.name = name
        self.area_id = area_id

    def json(self):
        obj = {
            'id': self.chamber_id,
            'name': {
                'en_US': self.name
            },
            'area_id': self.area_id
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "ChamberModel":
        return cls.query.filter_by(chamber_id=_id).first()

    @classmethod
    def find_all(cls) -> List["ChamberModel"]:
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
