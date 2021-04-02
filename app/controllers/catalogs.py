from app import app
from app.models.other_names_types import *

class Catalogue():

    def PopulateOtherNamesTypes():
        other_names_type1 = Other_Names_Types("preferred")
        other_names_type1.save()

        other_names_type2 = Other_Names_Types("nickname")
        other_names_type2.save()

        other_names_type3 = Other_Names_Types("ballot_name")
        other_names_type3.save()

"""
other_names = Other_Names_Types.query.all()
for name in other_names:
    print(str(name.other_names_type_id) + " " + name.description)
"""
