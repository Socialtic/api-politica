from app import ma
from app.models.contest import ContestModel

class ContestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ContestModel
        load_instance = True
        load_only = ("store",)
        include_fk = True