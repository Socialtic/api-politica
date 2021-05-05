from app import db
from typing import List
from app.const import URL_TYPE, URL_OWNER_TYPE, Catalogues

class UrlModel(db.Model):
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
        
    def json(self):
        obj = {
            'id': self.url_id,
            'url': self.url,
            'description': self.description,
            'url_type': Catalogues.URL_TYPE_FULL_NAMES[self.url_type],
            'owner_type': Catalogues.URL_OWNER_TYPE_NAMES[self.owner_type],
            'owner_id': self.owner_id
        }
        return obj

    @classmethod
    def find_by_id(cls, _id) -> "UrlModel":
        return cls.query.filter_by(url_id=_id).first()

    @classmethod
    def find_all(cls) -> List["UrlModel"]:
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

    @staticmethod
    def get_party_or_coalition_fb_urls(id, owner_type):
        urls = UrlModel.query.filter_by(url_type=URL_TYPE.FACEBOOK_CAMPAIGN, owner_type=owner_type, owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_party_or_coalition_ig_urls(id, owner_type):
        urls = UrlModel.query.filter_by(url_type=URL_TYPE.INSTAGRAM_CAMPAIGN, owner_type=owner_type, owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_party_or_coalition_logo_urls(id, owner_type):
        urls = UrlModel.query.filter_by(url_type=URL_TYPE.LOGO, owner_type=owner_type, owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_party_or_coalition_or_person_websites_urls(id, owner_type):
        urls_campaign = UrlModel.query.filter_by(url_type=URL_TYPE.WEBSITE_CAMPAIGN, owner_type=owner_type, owner_id=id)

        urls_official = UrlModel.query.filter_by(url_type=URL_TYPE.WEBSITE_OFFICIAL, owner_type=owner_type, owner_id=id)

        urls_personal = UrlModel.query.filter_by(url_type=URL_TYPE.WEBSITE_PERSONAL, owner_type=owner_type, owner_id=id)

        urls_wikipedia = UrlModel.query.filter_by(url_type=URL_TYPE.WEBSITE_WIKIPEDIA, owner_type=owner_type, owner_id=id)

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
        urls = UrlModel.query.filter_by(url_type=URL_TYPE.SOURCE_OF_TRUTH, owner_type=URL_OWNER_TYPE.MEMBERSHIP, owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_person_fb_urls(id):
        urls_campaign = UrlModel.query.filter_by(url_type=URL_TYPE.FACEBOOK_CAMPAIGN, owner_type=URL_OWNER_TYPE.PERSON, owner_id=id)

        urls_official = UrlModel.query.filter_by(url_type=URL_TYPE.FACEBOOK_OFFICIAL, owner_type=URL_OWNER_TYPE.PERSON, owner_id=id)

        urls_personal = UrlModel.query.filter_by(url_type=URL_TYPE.FACEBOOK_PERSONAL, owner_type=URL_OWNER_TYPE.PERSON, owner_id=id)

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
        urls_campaign = UrlModel.query.filter_by(url_type=URL_TYPE.INSTAGRAM_CAMPAIGN, owner_type=URL_OWNER_TYPE.PERSON, owner_id=id)

        urls_official = UrlModel.query.filter_by(url_type=URL_TYPE.INSTAGRAM_OFFICIAL, owner_type=URL_OWNER_TYPE.PERSON, owner_id=id)

        urls_personal = UrlModel.query.filter_by(url_type=URL_TYPE.INSTAGRAM_PERSONAL, owner_type=URL_OWNER_TYPE.PERSON, owner_id=id)

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
        urls = UrlModel.query.filter_by(url_type=URL_TYPE.PHOTO, owner_type=URL_OWNER_TYPE.PERSON, owner_id=id)
        result = []
        for url in urls:
            result.append(url.url)
        return result

    @staticmethod
    def get_person_social_networks_urls(id):

        urls = UrlModel.query.filter(UrlModel.url_type >= URL_TYPE.TWITTER, UrlModel.url_type <= URL_TYPE.RSS,
                                UrlModel.owner_type == URL_OWNER_TYPE.PERSON, UrlModel.owner_id == id)

        result = []
        for url in urls:
            obj = {
                'type': Catalogues.URL_TYPE_NAMES[url.url_type],
                'value': url.url
            }
            result.append(obj)
        return result
