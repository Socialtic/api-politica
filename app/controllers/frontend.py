from app import app

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
