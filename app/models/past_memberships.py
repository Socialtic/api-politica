from app import db
from datetime import date

class Past_Memberships(db.Model):
    __tablename__ = 'past_memberships'
    __table_args__ = {'sqlite_autoincrement': True}

    past_membership_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    party_name = db.Column(db.String(100), nullable=False)
    coalition_name = db.Column(db.String(100))
    role_name = db.Column(db.String(100), nullable=False)

    def __init__(self, person_id, start_date, end_date, party_name, coalition_name, role_name):
        self.person_id = person_id
        self.start_date = start_date
        self.end_date = end_date
        self.party_name = party_name
        self.coalition_name = coalition_name
        self.role_name = role_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        past_memberships = Past_Memberships.query.all()
        result = []
        for past_membership in past_memberships:
            obj = {
                'id': past_membership.past_membership_id,
                'person_id': past_membership.person_id,
                'start_date': past_membership.start_date.strftime('%Y-%m-%d'),
                'end_date': past_membership.end_date.strftime('%Y-%m-%d'),
                'party_name': past_membership.party_name,
                'coalition_name': past_membership.coalition_name,
                'role_name': past_membership.role_name
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()
