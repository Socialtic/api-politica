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

class URL_OWNER_TYPE:
    PERSON = 1
    PARTY = 2
    COALITION = 3
    MEMBERSHIP = 4

class URL_TYPE:
    WEBSITE_CAMPAIGN = 1
    WEBSITE_OFFICIAL = 2
    WEBSITE_PERSONAL = 3
    WEBSITE_WIKIPEDIA = 4
    FACEBOOK_CAMPAIGN = 5
    FACEBOOK_OFFICIAL = 6
    FACEBOOK_PERSONAL = 7
    INSTAGRAM_CAMPAIGN = 8
    INSTAGRAM_OFFICIAL = 9
    INSTAGRAM_PERSONAL = 10
    WHATSAPP = 11
    TWITTER = 12
    YOUTUBE = 13
    LINKEDIN = 14
    FLICKR = 15
    PINTEREST = 16
    TUMBLR = 17
    RSS = 18
    EMAIL = 19
    PHOTO = 20
    LOGO = 21
    SOURCE_OF_TRUTH = 22

class Catalogues:
    DEGREES_OF_STUDIES = ['', 'ELEMENTARY', 'HIGH SCHOOL', 'ASSOCIATE DEGREE', 'BACHELOR’S DEGREE', 'UNIVERSITY 1 ST PROFESSIONAL DEGREE', 'MASTER DEGREE', 'PHD DEGREE']
    #   GOBERNADOR, DIPUTADO , PRESIDENTE MUNICIPAL
    DISTRICT_TYPES = ['NATIONAL_EXEC', 'REGIONAL_EXEC', 'NATIONAL_LOWER', 'LOCAL_EXEC']
    GENDERS = ['', 'M', 'F']
    MEMBERSHIP_TYPES = ['', 'officeholder', 'campaigning_politician', 'party_leader']
    # privilegiado, apodo, nombre de la boleta
    OTHER_NAMES_TYPES = ['', 'preferred', 'nickname', 'ballot_name']
    #   GOBERNADOR, DIPUTADO , PRESIDENTE MUNICIPAL
    ROLE_TYPES = ['', 'governmentOfficer', 'legislatorLowerBody', 'executiveCouncil']
    URL_TYPE_NAMES = ['', 'campaign', 'official', 'personal', 'wikipedia']
