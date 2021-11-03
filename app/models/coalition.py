from app import db
from app.const import URL_OWNER_TYPE
from app.models.url import UrlModel

class CoalitionModel(db.Model):
    __tablename__ = 'coalition'
    __table_args__ = {'sqlite_autoincrement': True}

    coalition_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    abbreviation = db.Column(db.String(50))
    colors = db.Column(db.JSON)

    def __init__(self, name, abbreviation, colors):
        self.name = name
        self.abbreviation = abbreviation
        self.colors = colors

    def json(self):
        obj = {
            'id': self.coalition_id,
            'name': {
                'en_US': self.name,
                'es_AR': self.name
            },
            'abbreviation': {
                'en_US': self.abbreviation,
                'es_AR': self.abbreviation
            },
            'colors': self.colors,
            'fb_urls': UrlModel.get_party_or_coalition_fb_urls(self.coalition_id, URL_OWNER_TYPE.COALITION),
            'ig_urls': UrlModel.get_party_or_coalition_ig_urls(self.coalition_id, URL_OWNER_TYPE.COALITION),
            'logo_urls': UrlModel.get_party_or_coalition_logo_urls(self.coalition_id, URL_OWNER_TYPE.COALITION),
            'websites': UrlModel.get_party_or_coalition_or_person_websites_urls(self.coalition_id,URL_OWNER_TYPE.COALITION)
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "CoalitionModel":
        return cls.query.filter_by(coalition_id=_id).first()

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
