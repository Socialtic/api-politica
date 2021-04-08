from app import db

class Profession(db.Model):
    __tablename__ = 'profession'
    __table_args__ = {'sqlite_autoincrement': True}

    profession_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    description = db.Column(db.String, nullable=False)


    def __init__(self, description):
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        professions = Profession.query.all()
        result = []
        for profession in professions:
            obj = {
                'profession_id': profession.profession_id,
                'description': profession.description
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
