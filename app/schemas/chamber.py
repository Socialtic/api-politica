from app import ma
from app.models.chamber import ChamberModel

class ChamberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ChamberModel
        load_instance = True
        load_only = ("store",)
        include_fk = True