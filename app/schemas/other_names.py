from app import ma
from app.models.other_names import OtherNamesModel

class OtherNamesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = OtherNamesModel
        load_instance = True
        load_only = ("store",)
        include_fk = True