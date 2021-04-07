from app import db
from app.const import EmptyValues

class Party(db.Model):
    __tablename__ = 'party'
    __table_args__ = {'sqlite_autoincrement': True}

    party_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    abbreviation = db.Column(db.String)
    colors = db.Column(db.JSON)
    area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=True)
    coalition_id = db.Column(db.Integer, db.ForeignKey('coalition.coalition_id'), nullable=True)

    def __init__(self, name, abbreviation, colors, area_id, coalition_id):
        self.name = name
        self.abbreviation = abbreviation
        self.colors = colors
        self.area_id = area_id
        self.coalition_id = coalition_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        parties = Party.query.all()
        result = []
        for party in parties:
            obj = {
                'party_id': party.party_id,
                'name': {
                    'en_US': party.name,
                    'es_MX': party.name
                },
                'abbreviation': {
                    'en_US': party.abbreviation,
                    'es_MX': party.abbreviation
                },
                'colors': party.colors,
                'area_id': "" if party.area_id == EmptyValues.EMPTY_INT else party.area_id,
                'coalition_id': "" if party.coalition_id == EmptyValues.EMPTY_INT else party.coalition_id
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
