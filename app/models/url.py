from app import db
from app.const import URL_TYPE, URL_OWNER_TYPE, Catalogues

class Url(db.Model):
    __tablename__ = 'url'
    __table_args__ = {'sqlite_autoincrement': True}

    url_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    url = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    url_type = db.Column(db.Integer, nullable=False)
    owner_type = db.Column(db.Integer, nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)

    def __init__(self, url, description, url_type, owner_type, owner_id):
        self.url = url
        self.description = description
        self.url_type = url_type
        self.owner_type = owner_type
        self.owner_id = owner_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        urls = Url.query.all()
        result = []
        for url in urls:
            obj = {
                'id': url.url_id,
                'url': url.url,
                'description': url.description,
                'url_type': url.url_type,
                'owner_type': url.owner_type,
                'owner_id': url.owner_id
            }
            result.append(obj)
        return result

    @staticmethod
    def get_party_fb_urls(party_id):
        urls = Url.query.filter_by(url_type=URL_TYPE.FACEBOOK_CAMPAIGN, owner_type=URL_OWNER_TYPE.PARTY,
                                   owner_id=party_id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_party_ig_urls(party_id):
        urls = Url.query.filter_by(url_type=URL_TYPE.INSTAGRAM_CAMPAIGN, owner_type=URL_OWNER_TYPE.PARTY,
                                   owner_id=party_id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_party_logo_urls(party_id):
        urls = Url.query.filter_by(url_type=URL_TYPE.LOGO, owner_type=URL_OWNER_TYPE.PARTY,
                                   owner_id=party_id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_party_websites_urls(party_id):
        urls_campaign = Url.query.filter_by(url_type=URL_TYPE.WEBSITE_CAMPAIGN, owner_type=URL_OWNER_TYPE.PARTY,
                                            owner_id=party_id)

        urls_official = Url.query.filter_by(url_type=URL_TYPE.WEBSITE_OFFICIAL, owner_type=URL_OWNER_TYPE.PARTY,
                                            owner_id=party_id)

        urls_personal = Url.query.filter_by(url_type=URL_TYPE.WEBSITE_PERSONAL, owner_type=URL_OWNER_TYPE.PARTY,
                                            owner_id=party_id)

        urls_wikipedia = Url.query.filter_by(url_type=URL_TYPE.WEBSITE_WIKIPEDIA, owner_type=URL_OWNER_TYPE.PARTY,
                                            owner_id=party_id)

        result = []

        for url in urls_campaign:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.WEBSITE_CAMPAIGN],
                'url': url.url
            }
            result.append(obj)

        for url in urls_official:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.WEBSITE_OFFICIAL],
                'url': url.url
            }
            result.append(obj)

        for url in urls_personal:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.WEBSITE_PERSONAL],
                'url': url.url
            }
            result.append(obj)

        for url in urls_wikipedia:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.WEBSITE_WIKIPEDIA],
                'url': url.url
            }
            result.append(obj)

        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
