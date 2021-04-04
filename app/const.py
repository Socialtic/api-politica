class HttpStatus:
    OK = 200
    CREATED = 201
    NOT_FOUND = 404
    BAD_REQUEST = 400

class EmptyValues:
    EMPTY_INT = (-1)
    EMPTY_STRING = ''

class Catalogues:
    OTHER_NAMES_TYPES = ['','preferred', 'nickname', 'ballot_name']
    GENDERS = ['','M', 'F', 'B', 'N']
    #   https://www.gob.mx/sep/acciones-y-programas/educacion-por-niveles?state=published
    DEGREES_OF_STUDIES = ['','EDUCACIÓN INICIAL', 'EDUCACIÓN BÁSICA', 'EDUCACIÓN MEDIA SUPERIOR', 'EDUCACIÓN SUPERIOR', 'EDUCACIÓN TECNOLÓGICA', 'EDUCACIÓN INDÍGENA']
    PROFESSIONS = ['','INGENIEROS', 'ABOGADOS', 'MÉDICOS', 'ARQUITECTO', 'PERIODISTA', 'VETERINARIO', 'DENTISTA']
