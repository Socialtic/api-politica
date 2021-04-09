from app import db

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
                'description': url.description,
                'url_type': url.url_type,
                'owner_type': url.owner_type,
                'owner_id': url.owner_id
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
