from app import ma
from app.models.url import UrlModel

class UrlSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UrlModel
        load_instance = True
        load_only = ("store",)
        include_fk = True