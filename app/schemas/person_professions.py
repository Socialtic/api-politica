from app import ma
from app.models.person_professions import PersonProfessionModel

class PersonProfessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PersonProfessionModel
        load_instance = True
        load_only = ("store",)
        include_fk = True