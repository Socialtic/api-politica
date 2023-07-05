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
#database_file = "sqlite:///{}".format(os.path.join(project_dir, "db/database_campaign.db"))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "db/database_officeholders.db"))

#   Configure for RDS/AWS MySQL
#   format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
#database_file = 'mysql+pymysql://user:password@db_identifier.aws_zone.amazonaws.com:3306/db_name'

#   Config app
application = Flask(__name__)
application.config["SQLALCHEMY_DATABASE_URI"] = database_file
application.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
application.config['JSON_AS_ASCII'] = False
isOnDev = True
application.debug = isOnDev
application.register_blueprint(bp_frontend)
application.register_blueprint(bp_token)
CORS(application)
ma = Marshmallow(application)
db = SQLAlchemy(application)
api = Api(application, doc='/docs',
          title='MX Elections 2021',
          description='API of information on the Colombian elections of 2022',
          version='1.1')

#   Some kind of internal token
from app.models.token_auth import *

application.app_context().push
with application.app_context():
	try:
	    INTERNAL_TOKEN = TokenAuth.find_by_id(1)
	except:
	    INTERNAL_TOKEN = True

#   Functions for the app
from app.controllers.area import *
from app.controllers.chamber import *
from app.controllers.role import *
from app.controllers.coalition import *
from app.controllers.party import *
from app.controllers.person import *
from app.controllers.other_names import *
from app.controllers.professions import *
from app.controllers.person_professions import *
from app.controllers.memberships import *
from app.controllers.contest import *
from app.controllers.url import *
from app.controllers.export import *
