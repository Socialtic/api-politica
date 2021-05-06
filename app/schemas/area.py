from app import ma
from app.models.area import AreaModel

class AreaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AreaModel
        load_instance = True
        load_only = ("store",)
        include_fk = True