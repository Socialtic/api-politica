from app import ma
from app.models.memberships import MembershipModel

class MembershipSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MembershipModel
        load_instance = True
        load_only = ("store",)
        include_fk = True