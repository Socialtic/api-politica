from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# Classes for database
class PersonModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Person(first_name = {first_name}, last_name = {last_name}, age = {age})"

db.create_all() # just at first run

# Parsers
person_post_args = reqparse.RequestParser()
person_post_args.add_argument("first_name", type=str, help="First name of the person is required", required=True)
person_post_args.add_argument("last_name", type=str, help="Last name of the person is required", required=True)
person_post_args.add_argument("age", type=int, help="Age of the person is required", required=True)

person_update_args = reqparse.RequestParser()
person_update_args.add_argument("first_name", type=str, help="First name of the person")
person_update_args.add_argument("last_name", type=str, help="Last name of the person")
person_update_args.add_argument("age", type=int, help="Age of the person")

resource_fields = {
    'id': fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'age': fields.Integer
}

# Classes
class Person(Resource):
    @marshal_with(resource_fields) # Decorator to serialize
    def get(self, person_id):
        result = PersonModel.query.filter_by(id=person_id).first()
        if not result:
            abort(404, message="Could not find a person with that id ...")
        return result

    @marshal_with(resource_fields) # Decorator to serialize
    def post(self, person_id):
        args = person_post_args.parse_args()
        result = PersonModel.query.filter_by(id=person_id).first()
        if result:
            abort(409, message="Person id taken ...")
        #fn = args['first_name']
        ln = args['last_name']
        #ag = args['age']
        print(args)
        person = PersonModel(id=person_id, first_name=args['first_name'], last_name=ln, age=args['age'])
        db.session.add(person)
        db.session.commit()
        return person, 201

    @marshal_with(resource_fields) # Decorator to serialize
    def patch(self, person_id): # update
        args = person_update_args.parse_args()
        result = PersonModel.query.filter_by(id=person_id).first()

        #print(result)

        if not result:
            abort(404, message="Person doesnt exist, cannot update ...")

        if args['first_name']:
            result.first_name =  args['first_name']
            print("First name")
        if args['last_name']:
            result.last_name =  args['last_name']
            print("Last name")
        if args['age']:
            result.age =  args['age']
            print("Age")

        db.session.commit()

        return result

    def delete(self, person_id):
        result = PersonModel.query.filter_by(id=person_id).first()
        if not result:
            abort(404, message="Could not find a person with that id ...")
        db.session.delete(result)
        db.session.commit()

        return {}, 204

# Resources
api.add_resource(Person, "/person/<int:person_id>")

# Entry point
if __name__ == "__main__":
    app.run(debug=True)     # For testing
