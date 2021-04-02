from app import db

class Other_Names_Types(db.Model):
    __tablename__ = 'other_names_types'
    __table_args__ = {'sqlite_autoincrement': True}

    other_names_type_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    description = db.Column(db.String, nullable=False)

    def __init__(self, description):
        self.description = description

    def save(self):
        db.session.add(self)
        db.session.commit()
