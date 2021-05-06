from app import ma
from app.models.coalition import CoalitionModel

class CoalitionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CoalitionModel
        load_instance = True
        load_only = ("store",)
        include_fk = True