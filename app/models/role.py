from app import db
from app.const import Catalogues

class Role(db.Model):
    __tablename__ = 'role'
    __table_args__ = {'sqlite_autoincrement': True}

    role_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    role_type = db.Column(db.Integer, nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=False)
    chamber_id = db.Column(db.Integer, db.ForeignKey('chamber.chamber_id'), nullable=False)
    #contest_id = db.Column(db.Integer, db.ForeignKey('contest.contest_id'), nullable=True)
    contest_id = db.Column(db.Integer, nullable=True) # Change it to ForeignKey

    def __init__(self, title, role_type, area_id, chamber_id, contest_id):
        self.title = title
        self.role_type = role_type
        self.area_id = area_id
        self.chamber_id = chamber_id
        self.contest_id = contest_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        roles = Role.query.all()
        result = []
        for role in roles:
            obj = {
                'role_id': role.role_id,
                'title': {
                    'en_US': role.title
                },
                'role': Catalogues.ROLE_TYPES[role.role_type],
                'area_id': role.area_id,
                'chamber_id': role.chamber_id,
                'contest_id': role.contest_id
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
