from app import db

class Chamber(db.Model):
    __tablename__ = 'chamber'
    __table_args__ = {'sqlite_autoincrement': True}

    chamber_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=False)

    def __init__(self, name, area_id):
        self.name = name
        self.area_id = area_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        chambers = Chamber.query.all()
        result = []
        for chamber in chambers:
            obj = {
                'id': chamber.chamber_id,
                'name': {
                    'en_US': chamber.name
                },
                'area_id': chamber.area_id
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
