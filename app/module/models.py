from app import db

class Person(db.Model):
    __tablename__ = 'person' #Must be defined the table name

    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<name: {}>".format(self.name)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        persons = Person.query.all()
        result = []
        for person in persons:
            obj = {
                'id': person.id,
                'name': person.name
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
