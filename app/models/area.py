from app import db
from app.const import Catalogues, EmptyValues

class Area(db.Model):
    __tablename__ = 'area'
    __table_args__ = {'sqlite_autoincrement': True}

    area_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    ocd_id = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    state = db.Column(db.String)
    city = db.Column(db.String)
    district_type = db.Column(db.Integer, nullable=False)
    parent_area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=True)

    def __init__(self, ocd_id, name, country, state, city, district_type, parent_area_id):
        self.ocd_id = ocd_id
        self.name = name
        self.country = country
        self.state = state
        self.city = city
        self.district_type = district_type
        self.parent_area_id = parent_area_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        areas = Area.query.all()
        result = []
        for area in areas:
            obj = {
                'area_id': area.area_id,
                'ocd_id': area.ocd_id,
                'name': {
                    'en_US': area.name,
                    'es_MX': area.name
                },
                'country': area.country,
                'state': area.state,
                'city': area.city,
                'district_type': Catalogues.DISTRICT_TYPES[area.district_type],
                'parent_area_id': "" if area.parent_area_id == EmptyValues.EMPTY_INT else area.parent_area_id
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
