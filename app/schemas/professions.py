from app import ma
from app.models.professions import ProfessionModel

class ProfessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProfessionModel
        load_instance = True
        load_only = ("store",)
        include_fk = True