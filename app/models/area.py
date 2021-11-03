from app import db
from app.const import Catalogues, EmptyValues

class AreaModel(db.Model):
    __tablename__ = 'area'
    __table_args__ = {'sqlite_autoincrement': True}

    area_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    ocd_id = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(2), nullable=False)
    state = db.Column(db.String(5))
    city = db.Column(db.String(3000))
    district_type = db.Column(db.Integer, nullable=False)
    #parent_area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=True)
    parent_area_id = db.Column(db.Integer, nullable=True)

    def __init__(self, ocd_id, name, country, state, city, district_type, parent_area_id):
        self.ocd_id = ocd_id
        self.name = name
        self.country = country
        self.state = state
        self.city = city
        self.district_type = district_type
        self.parent_area_id = parent_area_id

    def json(self):
        obj = {
            'id': self.area_id,
            'ocd_id': self.ocd_id,
            'name': {
                'en_US': self.name,
                'es_AR': self.name
            },
            'country': self.country,
            'state': self.state,
            'city': self.city,
            'district_type': Catalogues.DISTRICT_TYPES[self.district_type],
            'parent_area_id': "" if self.parent_area_id == EmptyValues.EMPTY_INT else self.parent_area_id
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "AreaModel":
        return cls.query.filter_by(area_id=_id).first()

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
