from app import db

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
                'coalition_id': coalition.coalition_id,
                'name': coalition.name,
                'abbreviation': coalition.abbreviation,
                'colors': coalition.colors
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
