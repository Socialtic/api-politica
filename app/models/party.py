from app import db
from app.const import EmptyValues, URL_OWNER_TYPE
from app.models.url import UrlModel

class PartyModel(db.Model):
    __tablename__ = 'party'
    __table_args__ = {'sqlite_autoincrement': True}

    party_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    abbreviation = db.Column(db.String(50))
    colors = db.Column(db.JSON)
    area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=True)
    #coalition_id = db.Column(db.Integer, db.ForeignKey('coalition.coalition_id'), nullable=True)
    coalition_id = db.Column(db.Integer, nullable=True)

    def __init__(self, name, abbreviation, colors, area_id, coalition_id):
        self.name = name
        self.abbreviation = abbreviation
        self.colors = colors
        self.area_id = area_id
        self.coalition_id = coalition_id

    def json(self):
        obj = {
            'id': self.party_id,
            'name': {
                'en_US': self.name,
                'es_MX': self.name
            },
            'abbreviation': {
                'en_US': self.abbreviation,
                'es_MX': self.abbreviation
            },
            'colors': self.colors,
            'area_id': "" if self.area_id == EmptyValues.EMPTY_INT else self.area_id,
            'coalition_id': "" if self.coalition_id == EmptyValues.EMPTY_INT else self.coalition_id,
            'fb_urls': UrlModel.get_party_or_coalition_fb_urls(self.party_id, URL_OWNER_TYPE.PARTY),
            'ig_urls': UrlModel.get_party_or_coalition_ig_urls(self.party_id, URL_OWNER_TYPE.PARTY),
            'logo_urls': UrlModel.get_party_or_coalition_logo_urls(self.party_id, URL_OWNER_TYPE.PARTY),
            'websites': UrlModel.get_party_or_coalition_or_person_websites_urls(self.party_id, URL_OWNER_TYPE.PARTY)
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "PartyModel":
        return cls.query.filter_by(party_id=_id).first()

    @classmethod
    def find_all(cls):
        query_all = cls.query.all()
        result = []
        for one_element in query_all:
            result.append(one_element.json())
        return result

    @classmethod
    def find_officeholders(cls, _parties):
        result = []
        for party in _parties:
            result.append(cls.query.filter_by(party_id=party).first().json())
        return result

    def save(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete(self) -> None:
        db.session.delete(self)
        db.session.commit()
