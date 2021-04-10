from app import db
from app.controllers.url import *
from app.const import URL_OWNER_TYPE

class Coalition(db.Model):
    __tablename__ = 'coalition'
    __table_args__ = {'sqlite_autoincrement': True}

    coalition_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    abbreviation = db.Column(db.String)
    colors = db.Column(db.JSON)

    def __init__(self, name, abbreviation, colors):
        self.name = name
        self.abbreviation = abbreviation
        self.colors = colors

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        coalitions = Coalition.query.all()
        result = []
        for coalition in coalitions:
            obj = {
                'id': coalition.coalition_id,
                'name': coalition.name,
                'abbreviation': coalition.abbreviation,
                'colors': coalition.colors,
                'fb_urls': Url.get_party_or_coalition_fb_urls(coalition.coalition_id, URL_OWNER_TYPE.COALITION),
                'ig_urls': Url.get_party_or_coalition_ig_urls(coalition.coalition_id, URL_OWNER_TYPE.COALITION),
                'logo_urls': Url.get_party_or_coalition_logo_urls(coalition.coalition_id, URL_OWNER_TYPE.COALITION),
                'websites': Url.get_party_or_coalition_or_person_websites_urls(coalition.coalition_id,
                                                                               URL_OWNER_TYPE.COALITION)
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
