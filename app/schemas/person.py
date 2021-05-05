from app import ma
from app.models.person import PersonModel

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PersonModel
        load_instance = True
        load_only = ("store",)
        include_fk = True