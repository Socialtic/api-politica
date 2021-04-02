import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Config paths
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "db/database.db"))

# Config app
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers.frontend import *
from app.controllers.area import *
from app.controllers.chamber import *
from app.controllers.role import *

# For testing
#db.drop_all()
db.create_all()
