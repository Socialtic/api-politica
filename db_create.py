from app import db

print('Drop all')
db.drop_all()

print('Create all')
db.create_all()

print('Done')