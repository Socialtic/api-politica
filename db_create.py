from app import db
from app.models.token_auth import TokenAuth

print('Drop all')
db.drop_all()

print('Create all')
db.create_all()

print("Token time")
token_type = "Bearer"
token_token = input("Enter token: ")
token = TokenAuth(token_type, token_token)
token.save()

print('Done')