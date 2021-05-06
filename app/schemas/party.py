from app import ma
from app.models.party import PartyModel

class PartySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PartyModel
        load_instance = True
        load_only = ("store",)
        include_fk = True