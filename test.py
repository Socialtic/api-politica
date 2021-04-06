import requests
import json
from datetime import date

BASE = 'http://127.0.0.1:8000/'

print('-----------------------------------------------------------------------')
print('Inserting areas')
data = [
    {
    	'ocd_id': 'ocd-division/country:mx/state:bc',
    	'name': 'Baja California',
    	'country': 'México',
    	'state': 'Baja California',
    	'city': '',
    	'district_type': 'REGIONAL_EXECUTIVE',
    	'parent_area_id': ''
    },
    {
    	'ocd_id': 'ocd-division/country:mx/state:bc/fed:4',
    	'name': 'Tijuana',
    	'country': 'México',
    	'state': 'Baja California',
    	'city': 'Tijuana',
    	'district_type': 'NATIONAL_LOWER',
    	'parent_area_id': '1'
    },
    {
    	'ocd_id': 'ocd-division/country:mx/state:bc/city:4',
    	'name': 'Tijuana',
    	'country': 'México',
    	'state': 'Baja California',
    	'city': 'Tijuana',
    	'district_type': 'LOCAL_EXECUTIVE',
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
    	'name': 'Gubernatura de Baja California',
    	'area_id': '1'
    },
    {
    	'name': 'Diputación del Distrito Federal IV de Baja California',
    	'area_id': '2'
    },
    {
    	'name': 'Presidencia del municipio 4 de Bajalifornia (Tijuana)',
    	'area_id': '3'
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
    	'title': 'Gobernador',
    	'role': 'governmentOfficer',
    	'area_id': 1,
    	'chamber_id': 1,
    	'contest_id': ''
    },
    {
    	'title': 'Diputado',
    	'role': 'Diputado',
    	'area_id': 2,
    	'chamber_id': 2,
    	'contest_id': ''
    },
    {
    	'title': 'Presidente Municipal',
    	'role': 'executiveCouncil',
    	'area_id': 3,
    	'chamber_id': 3,
    	'contest_id': ''
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
    	'name': 'Va por México',
    	'abbreviation': 'VPM',
    	'colors': ['BLUE', 'RED', 'YELLOW']
    },
    {
    	'name': 'Juntos Hacemos Historia',
    	'abbreviation': 'JHH',
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
    	'name': 'Partido Revolucionario Institucional',
    	'abbreviation': 'PRI',
    	'colors': ['GREEN', 'WHITE', 'RED'],
    	'area_id': '1',
    	'coalition_id': '1'
    },
    {
    	'name': 'Partido Acción Nacional',
    	'abbreviation': 'PAN',
    	'colors': ['BLUE', 'WHITE'],
    	'area_id': '1',
    	'coalition_id': '1'
    },
    {
    	'name': 'Partido de la Revolución Democrática',
    	'abbreviation': 'PRD',
    	'colors': ['YELLOW', 'BLACK', 'RED'],
    	'area_id': '1',
    	'coalition_id': '1'
    },
    {
    	'name': 'Movimiento Regeneración Nacional',
    	'abbreviation': 'Morena',
    	'colors': ['RED'],
    	'area_id': '1',
    	'coalition_id': '2'
    },
    {
    	'name': 'Partido del Trabajo',
    	'abbreviation': 'PT',
    	'colors': ['RED', 'YELLOW'],
    	'area_id': '1',
    	'coalition_id': '2'
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
    	'full_name': 'Paul Aguilar',
    	'date_birth': '1994-02-16',
    	'gender': 1,
    	'dead_or_alive': True,
    	'last_degree_of_studies': 1,
    	'contest_id': ''
    },
    {
    	'full_name': 'Haydeé Quijano',
    	'date_birth': '1994-02-16',
    	'gender': 2,
    	'dead_or_alive': True,
    	'last_degree_of_studies': 2,
    	'contest_id': ''
    },
    {
    	'full_name': 'Jose Luis Pérez',
    	'date_birth': '1994-02-16',
    	'gender': 3,
    	'dead_or_alive': False,
    	'last_degree_of_studies': 3,
    	'contest_id': ''
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + 'person', json=data[i])
    print(response.json())
print('-----------------------------------------------------------------------')
print()

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

print('-----------------------------------------------------------------------')
print('Inserting memberships')
data = [
	{
		'person_id': 1,
		'role_id': 1,
		'party_id': 1,
		'coalition_id': 1,
		'goes_for_coalition': False,
		'membership_type': 1,
		'goes_for_reelection': False,
		'start_date': '',
		'end_date': '',
		'is_substitute': False,
		'parent_membership_id': '',
		'changed_from_substitute': False,
		'date_changed_from_substitute': ''
	},
	{
		'person_id': 2,
		'role_id': 2,
		'party_id': 2,
		'coalition_id': 2,
		'goes_for_coalition': False,
		'membership_type': 2,
		'goes_for_reelection': False,
		'start_date': '',
		'end_date': '',
		'is_substitute': False,
		'parent_membership_id': '',
		'changed_from_substitute': False,
		'date_changed_from_substitute': ''
	},
	{
		'person_id': 3,
		'role_id': 3,
		'party_id': 3,
		'coalition_id': 3,
		'goes_for_coalition': False,
		'membership_type': 3,
		'goes_for_reelection': False,
		'start_date': '',
		'end_date': '',
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

'''
requests.get
requests.post
requests.patch
requests.delete
'''
