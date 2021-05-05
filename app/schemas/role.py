from app import ma
from app.models.role import RoleModel

class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RoleModel
        load_instance = True
        load_only = ("store",)
        include_fk = True