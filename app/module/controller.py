from flask import request, jsonify
from app import app
from .models import *
from .const import HttpStatus

## <-- home/index --> ###
@app.route('/', methods=['GET', 'POST'])
def index():
    indexBody = """
<h1>Bienvenidx a la API abierta de las elecciones de México 2021</h1>
</br>
Para conocer más acerca del proyecto, te recomendamos visitar el repositorio de GitHhub o nuestras redes sociales.
</br>
<ul>
    <li><a href="https://github.com/SocialTIC/mx-elections-2021">Repositorio de GitHub del proyecto</a></li>
    <li><a href="https://socialtic.org">Sitio de SocialTIC</a></li>
    <li><a href="https://www.facebook.com/Socialtic/">Facebook de SocialTIC</a></li>
    <li><a href="https://twitter.com/socialtic/">Twitter de SocialTIC</a></li>
    <li><a href="https://www.instagram.com/socialtic/">Instagram de SocialTIC</a></li>
</ul>
<pre>
           __________
         .'----------`.
         | .--------. |
         | |########| |
         | |########| |      /__________\\
.--------| `--------' |------|    --=-- |-------------.
|        `----,-.-----'      |o ======  |             |
|       ______|_|_______     |__________|             |
|      /  %%%%%%%%%%%%  \                             |
|     /  %%%%%%%%%%%%%%  \                            |
|     ^^^^^^^^^^^^^^^^^^^^                            |
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
</pre>
    """
    return indexBody

## <-- person --> ###
@app.route('/person', methods=['GET', 'POST'])
def person():
    if request.method == 'GET':
        construct = {
            'error': [],
            'success': True,
            'persons': Person.getAll()
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK

    elif request.method == 'POST':
        name = None if request.json['name'] is "" else request.json['name']
        construct = {}
        try:
            person = Person(name=name)
            person.save()
            construct['success'] = True
            construct['message'] = 'Data saved'
            response = jsonify(construct)
            response.status_code = HttpStatus.CREATED
            print("<name: {}>".format(name))
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
    return response

@app.route('/person/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def personId(id):
    person = Person.query.filter_by(id=id).first()
    if request.method == 'GET':
        construct = {
            'error': [],
            'success': True,
            'person': {
                'id': person.id,
                'name': person.name
            }
        }
        response = jsonify(construct)
        response.status_code = HttpStatus.OK
    elif request.method == 'PUT':
        name = None if request.json['name'] is "" else request.json['name']
        construct = {}
        try:
            person.name = name
            db.session.commit()
            construct['success'] = True
            construct['message'] = 'Data saved'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
    elif request.method == 'DELETE':
        construct = {}
        try:
            person.delete()
            construct['success'] = True
            construct['message'] = 'Data has been delete.'
            response = jsonify(construct)
            response.status_code = HttpStatus.OK
        except Exception as e:
            construct['success'] = False
            construct['error'] = str(e)
            response = jsonify(construct)
            response.status_code = HttpStatus.BAD_REQUEST
    return response
