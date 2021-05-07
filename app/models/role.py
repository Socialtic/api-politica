from app import db
from typing import List
from app.const import Catalogues, EmptyValues

class RoleModel(db.Model):
    __tablename__ = 'role'
    __table_args__ = {'sqlite_autoincrement': True}

    role_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    role = db.Column(db.Integer, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=False)
    chamber_id = db.Column(db.Integer, db.ForeignKey('chamber.chamber_id'), nullable=False)
    #contest_id = db.Column(db.Integer, db.ForeignKey('contest.contest_id'), nullable=True)
    contest_id = db.Column(db.Integer, nullable=True) # Change it to ForeignKey

    def __init__(self, title, role, area_id, chamber_id, contest_id):
        self.title = title
        self.role = role
        self.area_id = area_id
        self.chamber_id = chamber_id
        self.contest_id = contest_id

    def json(self):
        obj = {
            'id': self.role_id,
            'title': {
                'en_US': self.title
            },
            'role': Catalogues.ROLE_TYPES[self.role],
            'area_id': self.area_id,
            'chamber_id': self.chamber_id,
            'contest_id': "" if self.contest_id == EmptyValues.EMPTY_INT else self.contest_id
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "RoleModel":
        return cls.query.filter_by(role_id=_id).first()

    @classmethod
    def find_all(cls) -> List["RoleModel"]:
        query_all = cls.query.all()
        result = []
        for one_element in query_all:
            result.append(one_element.json())
        return result

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
