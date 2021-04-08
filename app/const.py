class HttpStatus:
    OK = 200
    CREATED = 201
    NOT_FOUND = 404
    BAD_REQUEST = 400

class EmptyValues:
    EMPTY_INT = (-1)
    EMPTY_STRING = ''
    EMPTY_DATE = '0001-01-01'

class OtherNames:
    PREFERRED = 1
    NICKNAME = 2
    BALLOT_NAME = 3

class Catalogues:
    DEGREES_OF_STUDIES = ['', 'ELEMENTARY', 'HIGH SCHOOL', 'ASSOCIATE DEGREE', 'BACHELOR’S DEGREE', 'UNIVERSITY 1 ST PROFESSIONAL DEGREE', 'MASTER DEGREE', 'PHD DEGREE']
    #   GOBERNADOR, DIPUTADO , PRESIDENTE MUNICIPAL
    DISTRICT_TYPES = ['', 'REGIONAL_EXECUTIVE', 'NATIONAL_LOWER', 'LOCAL_EXECUTIVE']
    GENDERS = ['', 'M', 'F']
    MEMBERSHIP_TYPES = ['', 'campaigning_politician', 'officeholder_substitute', 'officeholder']
    # privilegiado, apodo, nombre de la boleta
    OTHER_NAMES_TYPES = ['', 'preferred', 'nickname', 'ballot_name']
    PROFESSIONS = ['', 'INGENIEROS', 'ABOGADOS', 'MÉDICOS', 'ARQUITECTO', 'PERIODISTA', 'VETERINARIO', 'DENTISTA']
    #   GOBERNADOR, DIPUTADO , PRESIDENTE MUNICIPAL
    ROLE_TYPES = ['', 'governmentOfficer', 'legislatorUpperBody', 'executiveCouncil']
