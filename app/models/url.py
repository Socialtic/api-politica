from app import db
from app.const import URL_TYPE, URL_OWNER_TYPE, Catalogues

class Url(db.Model):
    __tablename__ = 'url'
    __table_args__ = {'sqlite_autoincrement': True}

    url_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.String(500))
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
                'url_type': Catalogues.URL_TYPE_FULL_NAMES[url.url_type],
                'owner_type': Catalogues.URL_OWNER_TYPE_NAMES[url.owner_type],
                'owner_id': url.owner_id
            }
            result.append(obj)
        return result

    @staticmethod
    def get_party_or_coalition_fb_urls(id, owner_type):
        urls = Url.query.filter_by(url_type=URL_TYPE.FACEBOOK_CAMPAIGN, owner_type=owner_type,
                                   owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_party_or_coalition_ig_urls(id, owner_type):
        urls = Url.query.filter_by(url_type=URL_TYPE.INSTAGRAM_CAMPAIGN, owner_type=owner_type,
                                   owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_party_or_coalition_logo_urls(id, owner_type):
        urls = Url.query.filter_by(url_type=URL_TYPE.LOGO, owner_type=owner_type,
                                   owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_party_or_coalition_or_person_websites_urls(id, owner_type):
        urls_campaign = Url.query.filter_by(url_type=URL_TYPE.WEBSITE_CAMPAIGN, owner_type=owner_type,
                                            owner_id=id)

        urls_official = Url.query.filter_by(url_type=URL_TYPE.WEBSITE_OFFICIAL, owner_type=owner_type,
                                            owner_id=id)

        urls_personal = Url.query.filter_by(url_type=URL_TYPE.WEBSITE_PERSONAL, owner_type=owner_type,
                                            owner_id=id)

        urls_wikipedia = Url.query.filter_by(url_type=URL_TYPE.WEBSITE_WIKIPEDIA, owner_type=owner_type,
                                            owner_id=id)

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

    @staticmethod
    def get_membership_source_urls(id):
        urls = Url.query.filter_by(url_type=URL_TYPE.SOURCE_OF_TRUTH, owner_type=URL_OWNER_TYPE.MEMBERSHIP,
                                   owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_person_fb_urls(id):
        urls_campaign = Url.query.filter_by(url_type=URL_TYPE.FACEBOOK_CAMPAIGN, owner_type=URL_OWNER_TYPE.PERSON,
                                            owner_id=id)

        urls_official = Url.query.filter_by(url_type=URL_TYPE.FACEBOOK_OFFICIAL, owner_type=URL_OWNER_TYPE.PERSON,
                                            owner_id=id)

        urls_personal = Url.query.filter_by(url_type=URL_TYPE.FACEBOOK_PERSONAL, owner_type=URL_OWNER_TYPE.PERSON,
                                            owner_id=id)

        result = []

        for url in urls_campaign:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.FACEBOOK_CAMPAIGN],
                'url': url.url
            }
            result.append(obj)

        for url in urls_official:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.FACEBOOK_OFFICIAL],
                'url': url.url
            }
            result.append(obj)

        for url in urls_personal:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.FACEBOOK_PERSONAL],
                'url': url.url
            }
            result.append(obj)

        return result

    @staticmethod
    def get_person_ig_urls(id):
        urls_campaign = Url.query.filter_by(url_type=URL_TYPE.INSTAGRAM_CAMPAIGN, owner_type=URL_OWNER_TYPE.PERSON,
                                            owner_id=id)

        urls_official = Url.query.filter_by(url_type=URL_TYPE.INSTAGRAM_OFFICIAL, owner_type=URL_OWNER_TYPE.PERSON,
                                            owner_id=id)

        urls_personal = Url.query.filter_by(url_type=URL_TYPE.INSTAGRAM_PERSONAL, owner_type=URL_OWNER_TYPE.PERSON,
                                            owner_id=id)

        result = []

        for url in urls_campaign:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.INSTAGRAM_CAMPAIGN],
                'url': url.url
            }
            result.append(obj)

        for url in urls_official:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.INSTAGRAM_OFFICIAL],
                'url': url.url
            }
            result.append(obj)

        for url in urls_personal:
            obj = {
                'note': Catalogues.URL_TYPE_NAMES[URL_TYPE.INSTAGRAM_PERSONAL],
                'url': url.url
            }
            result.append(obj)

        return result

    @staticmethod
    def get_person_photo_urls(id):
        urls = Url.query.filter_by(url_type=URL_TYPE.PHOTO, owner_type=URL_OWNER_TYPE.PERSON,
                                   owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_person_social_networks_urls(id):

        urls = Url.query.filter(Url.url_type >= URL_TYPE.TWITTER, Url.url_type <= URL_TYPE.RSS,
                                Url.owner_type == URL_OWNER_TYPE.PERSON, Url.owner_id == id)

        result = []
        for url in urls:
            obj = {
                'type': Catalogues.URL_TYPE_NAMES[url.url_type],
                'value': url.url
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
