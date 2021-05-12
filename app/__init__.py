import os
from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from app.controllers.frontend import *
from app.controllers.token import *

#   Configure for local test
#   This works with SQLite3
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "db/database.db"))

#   Configure for RDS/AWS MySQL
#   format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
#database_file = 'mysql+pymysql://user:password@db_identifier.aws_zone.amazonaws.com:3306/db_name'


#   Config app
application = Flask(__name__)
application.config["SQLALCHEMY_DATABASE_URI"] = database_file
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
application.config['JSON_AS_ASCII'] = False
isOnDev = False
application.debug = isOnDev
application.register_blueprint(bp_frontend)
application.register_blueprint(bp_token)
CORS(application)
ma = Marshmallow(application)
db = SQLAlchemy(application)
api = Api(application, doc='/docs',
          title='MX Elections 2021',
          description='API of information on the Mexican elections of 2021',
          version='1.1')

#   Some kind of internal token
from app.models.token_auth import TokenAuth

try:
    INTERNAL_TOKEN = TokenAuth.find_by_id(1)
except:
    INTERNAL_TOKEN = True

#   Functions for the app
from app.controllers.area import Area, AreaList
from app.controllers.chamber import Chamber, ChamberList
from app.controllers.role import Role, RoleList
from app.controllers.coalition import Coalition, CoalitionList
from app.controllers.party import Party, PartyList
from app.controllers.person import Person, PersonList
from app.controllers.other_names import OtherNames, OtherNamesList
from app.controllers.professions import Profession, ProfessionList
from app.controllers.person_professions import PersonProfession, PersonProfessionList
from app.controllers.memberships import Membership, MembershipList
from app.controllers.contest import Contest, ContestList
from app.controllers.url import Url, UrlList
from app.controllers.export import Export, ExportMin