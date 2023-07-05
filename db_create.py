from app import application
from app import db
from app.models.token_auth import TokenAuth

# Creating context for application
application.app_context().push
with application.app_context():
	# Initializing DB
	print('Drop all')
	db.drop_all()

	print('Create all')
	db.create_all()

	# Initializing Token
	print("Token time")
	token_type = "Bearer"
	token_token = input("Enter token: ")
	token = TokenAuth(token_type, token_token)
	token.save()

	print('Done')
