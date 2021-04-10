import requests
from app.const import URL_TYPE, URL_OWNER_TYPE

BASE = 'http://127.0.0.1:8000/'

print('-----------------------------------------------------------------------')
print('Inserting areas')
data = [
    {
    	'ocd_id': 'ocd-division/country:mx',
    	'name': 'MÉXICO',
    	'country': 'MX',
    	'state': '',
    	'city': '',
    	'district_type': 0,
    	'parent_area_id': ''
    },
    {
    	'ocd_id': 'ocd-division/country:mx/state:bc',
    	'name': 'BAJA CALIFORNIA',
    	'country': 'MX',
    	'state': 'BCN',
    	'city': 'BAJA CALIFORNIA',
    	'district_type': 1,
    	'parent_area_id': '1'
    },
    {
    	'ocd_id': 'ocd-division/country:mx/state:bs',
    	'name': 'BAJA CALIFORNIA SUR',
    	'country': 'MX',
    	'state': 'BCS',
    	'city': 'BAJA CALIFORNIA SUR',
    	'district_type': 1,
    	'parent_area_id': '1'
    },
    {
    	'ocd_id': 'ocd-division/country:mx/state:cm',
    	'name': 'CAMPECHE',
    	'country': 'MX',
    	'state': 'BCS',
    	'city': 'CAM',
    	'district_type': 1,
    	'parent_area_id': '1'
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'area', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Inserting chambers')
data = [
    {
    	'name': 'Gubernatura de BAJA CALIFORNIA',
    	'area_id': '2'
    },
    {
    	'name': 'Gubernatura de BAJA CALIFORNIA SUR',
    	'area_id': '3'
    },
    {
    	'name': 'Gubernatura de CAMPECHE',
    	'area_id': '4'
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'chamber', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Inserting roles')
data = [
    {
    	'title': 'governmentOfficer',
    	'role': 1,
    	'area_id': 2,
    	'chamber_id': 1,
    	'contest_id': 1
    },
    {
    	'title': 'governmentOfficer',
    	'role': 1,
    	'area_id': 3,
    	'chamber_id': 2,
    	'contest_id': 2
    },
    {
    	'title': 'governmentOfficer',
    	'role': 1,
    	'area_id': 4,
    	'chamber_id': 3,
    	'contest_id': 3
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'role', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Inserting coalitions')
data = [
    {
    	'name': 'Candidatura común',
    	'abbreviation': '',
    	'colors': ['BLUE', 'RED', 'YELLOW']
    },
    {
    	'name': 'Equipo por el bien de Nuevo León',
    	'abbreviation': '',
    	'colors': ''
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'coalition', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()


print('-----------------------------------------------------------------------')
print('Inserting parties')
data = [
    {
    	'name': 'Movimiento de Regeneración Nacional',
    	'abbreviation': 'Morena',
    	'colors': ['RED'],
    	'area_id': '1',
    	'coalition_id': ''
    },
    {
    	'name': 'Movimiento Ciudadano',
    	'abbreviation': 'MC',
    	'colors': ['ORANGE'],
    	'area_id': '1',
    	'coalition_id': ''
    },
    {
    	'name': 'Partido Acción Nacional',
    	'abbreviation': 'PAN',
    	'colors': ['BLUE', 'WHITE'],
    	'area_id': '1',
    	'coalition_id': ''
    },
    {
    	'name': 'Partido de la Revolución Democrática',
    	'abbreviation': 'prd',
    	'colors': ['YELLOW', 'BLACK'],
    	'area_id': '1',
    	'coalition_id': ''
    },
    {
    	'name': 'Partido Encuentro Social',
    	'abbreviation': 'PES',
    	'colors': ['BLUE', 'WHITE'],
    	'area_id': '1',
    	'coalition_id': ''
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'party', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Inserting persons')
data = [
    {
    	'full_name': 'Marina del Pilar Ávila Olmeda',
		'first_name': 'Marina del Pilar',
		'last_name': 'Ávila',
    	'date_birth': '1985-09-19',
    	'gender': 2,
    	'dead_or_alive': True,
    	'last_degree_of_studies': 6,
    	'contest_id': 1
    },
    {
    	'full_name': 'Francisco Alcibiades Garcia Lizardi',
		'first_name': 'Franco',
		'last_name': 'Garcia',
    	'date_birth': '1941-12-17',
    	'gender': 1,
    	'dead_or_alive': True,
    	'last_degree_of_studies': 4,
    	'contest_id': 2
    },
    {
    	'full_name': 'María Guadalupe Jones Garay',
		'first_name': 'María',
		'last_name': 'Jones',
    	'date_birth': '1967-09-06',
    	'gender': 1,
    	'dead_or_alive': True,
    	'last_degree_of_studies': 6,
    	'contest_id': 3
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'person', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Inserting other names')
data = [
	{
		'other_name_type': 2,
		'name': 'Lupita Jones',
		'person_id': 3
	}
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'other-name', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Inserting professions')
data = [
	{
		'description': 'Didactics and pedagogy'
	},
	{
		'description': 'Educational planning and evaluation'
	},
	{
		'description': 'Educational counseling and guidance'
	}
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'profession', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Inserting person professions')
data = [
	{
		'person_id': 1,
		'profession_id': 1
	},
	{
		'person_id': 1,
		'profession_id': 2
	},
	{
		'person_id': 2,
		'profession_id': 2
	}
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'person-profession', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

"""
print('-----------------------------------------------------------------------')
print('Inserting past memberships')
data = [
    {
    	'person_id': 1,
    	'start_date': '2004-06-01',
    	'end_date': '2008-12-01',
    	'party_name': 'PRI',
    	'coalition_name': '',
    	'role_name': 'Presidente Municipal de Zapopan'
    },
    {
    	'person_id': 1,
    	'start_date': '2008-06-01',
    	'end_date': '2012-12-01',
    	'party_name': 'PRI',
    	'coalition_name': '',
    	'role_name': 'Gobernador de Jalisco'
    },
    {
    	'person_id': 1,
    	'start_date': '2012-06-01',
    	'end_date': '2018-12-01',
    	'party_name': 'PRI',
    	'coalition_name': '',
    	'role_name': 'Presidente de México'
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'past-membership', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()
"""

print('-----------------------------------------------------------------------')
print('Inserting memberships')
data = [
	{
		'person_id': 1,
		'role_id': 2,
		'party_id': 4,
		'coalition_id': '',
		'contest_id': 1,
		'goes_for_coalition': True,
		'membership_type': 2,
		'goes_for_reelection': False,
		'start_date': '2020-04-04',
		'end_date': '2020-06-02',
		'is_substitute': False,
		'parent_membership_id': '',
		'changed_from_substitute': False,
		'date_changed_from_substitute': ''
	},
	{
		'person_id': 2,
		'role_id': 2,
		'party_id': 2,
		'coalition_id': '',
		'contest_id': 2,
		'goes_for_coalition': True,
		'membership_type': 2,
		'goes_for_reelection': False,
		'start_date': '2020-04-05',
		'end_date': '2020-06-02',
		'is_substitute': False,
		'parent_membership_id': '',
		'changed_from_substitute': False,
		'date_changed_from_substitute': ''
	},
	{
		'person_id': 3,
		'role_id': 2,
		'party_id': 1,
		'coalition_id': '',
		'contest_id': 3,
		'goes_for_coalition': True,
		'membership_type': 2,
		'goes_for_reelection': False,
		'start_date': '2020-04-06',
		'end_date': '2020-06-02',
		'is_substitute': False,
		'parent_membership_id': '',
		'changed_from_substitute': False,
		'date_changed_from_substitute': ''
	}
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'membership', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Inserting contests')
data = [
	{
		'area_id': 2,
		'title': 'Gubernatura de BAJA CALIFORNIA',
		'membership_id_winner': '',
		'start_date': '2020-04-05',
		'end_date': '2020-06-06',
		'election_identifier': 'election-identifier-01'
	},
	{
		'area_id': 2,
		'title': 'Gubernatura de BAJA CALIFORNIA SUR',
		'membership_id_winner': '',
		'start_date': '2020-04-05',
		'end_date': '2020-06-06',
		'election_identifier': 'election-identifier-02'
	},
	{
		'area_id': 3,
		'title': 'Gubernatura de CAMPECHE',
		'membership_id_winner': '',
		'start_date': '2020-04-05',
		'end_date': '2020-06-06',
		'election_identifier': 'election-identifier-03'
	}
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'contest', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

print('-----------------------------------------------------------------------')
print('Inserting urls')
data = [
	{
		'url': 'https://facebook.com/partido',
		'description': 'Página de FB del partido',
		'url_type': URL_TYPE.FACEBOOK_CAMPAIGN,
		'owner_type': URL_OWNER_TYPE.PARTY,
		'owner_id': 1
	},
	{
		'url': 'https://instagram.com/partido',
		'description': 'Página de IG del partido',
		'url_type': URL_TYPE.INSTAGRAM_CAMPAIGN,
		'owner_type': URL_OWNER_TYPE.PARTY,
		'owner_id': 1
	},
	{
		'url': 'https://partido.com/logo.png',
		'description': 'Logo del partido',
		'url_type': URL_TYPE.LOGO,
		'owner_type': URL_OWNER_TYPE.PARTY,
		'owner_id': 1
	},
	{
		'url': 'https://sitio-campania.com/',
		'description': 'Sitio de campaña del partido',
		'url_type': URL_TYPE.WEBSITE_CAMPAIGN,
		'owner_type': URL_OWNER_TYPE.PARTY,
		'owner_id': 1
	},
	{
		'url': 'https://sitio-oficial.com/',
		'description': 'Sitio oficial del  partido',
		'url_type': URL_TYPE.WEBSITE_OFFICIAL,
		'owner_type': URL_OWNER_TYPE.PARTY,
		'owner_id': 1
	},
	{
		'url': 'https://sitio-personal.com/',
		'description': 'Sitio personal del partido',
		'url_type': URL_TYPE.WEBSITE_PERSONAL,
		'owner_type': URL_OWNER_TYPE.PARTY,
		'owner_id': 1
	},
	{
		'url': 'https://sitio-wikipedia.com/',
		'description': 'Sitio de wikipedoa del partido',
		'url_type': URL_TYPE.WEBSITE_WIKIPEDIA,
		'owner_type': URL_OWNER_TYPE.PARTY,
		'owner_id': 1
	}
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'url', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

'''
requests.get
requests.post
requests.patch
requests.delete
'''
