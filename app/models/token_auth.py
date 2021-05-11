from app import db

class TokenAuth(db.Model):
    __tablename__ = 'token_auth'

    token_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    type = db.Column(db.String(20), nullable=False)
    token = db.Column(db.String(100), nullable=False)

    def __init__(self, type, token):
        self.type = type
        self.token = token

    @classmethod
    def find_by_id(cls, _id) -> "TokenAuth":
        return cls.query.filter_by(token_id=_id).first()

    def compare(self, header_token):
        try:
            full_token = self.type + " " + self.token
            if full_token == header_token:
                return True
            else:
                return False
        except Exception as e:
            return False

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
