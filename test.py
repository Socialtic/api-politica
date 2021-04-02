import requests

BASE = "http://127.0.0.1:8000/"

print("-----------------------------------------------------------------------")
print("Inserting areas")
data = [
    {
    	"ocd_id": "ocd-division/country:mx/state:bc",
    	"name": "Baja California",
    	"country": "México",
    	"state": "Baja California",
    	"city": "",
    	"distric_type": "REGIONAL_EXECUTIVE",
    	"parent_area_id": ""
    },
    {
    	"ocd_id": "ocd-division/country:mx/state:bc/fed:4",
    	"name": "Tijuana",
    	"country": "México",
    	"state": "Baja California",
    	"city": "Tijuana",
    	"distric_type": "NATIONAL_LOWER",
    	"parent_area_id": ""
    },
    {
    	"ocd_id": "ocd-division/country:mx/state:bc/city:4",
    	"name": "Tijuana",
    	"country": "México",
    	"state": "Baja California",
    	"city": "Tijuana",
    	"distric_type": "LOCAL_EXECUTIVE",
    	"parent_area_id": ""
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + "area", json=data[i])
    print(response.json())
print("-----------------------------------------------------------------------")
print()

print("-----------------------------------------------------------------------")
print("Inserting chambers")
data = [
    {
    	"name": "Gubernatura de Baja California",
    	"area_id": "1"
    },
    {
    	"name": "Diputación del Distrito Federal IV de Baja California",
    	"area_id": "2"
    },
    {
    	"name": "Presidencia del municipio 4 de Bajalifornia (Tijuana)",
    	"area_id": "3"
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + "chamber", json=data[i])
    print(response.json())
print("-----------------------------------------------------------------------")
print()

print("-----------------------------------------------------------------------")
print("Inserting roles")
data = [
    {
    	"title": "Gobernador",
    	"role": "governmentOfficer",
    	"area_id": 1,
    	"chamber_id": 1,
    	"contest_id": ""
    },
    {
    	"title": "Diputado",
    	"role": "Diputado",
    	"area_id": 2,
    	"chamber_id": 2,
    	"contest_id": ""
    },
    {
    	"title": "Presidente Municipal",
    	"role": "executiveCouncil",
    	"area_id": 3,
    	"chamber_id": 3,
    	"contest_id": ""
    }
]

for i in range(len(data)):
    print(data[i])
    response = requests.post(BASE + "role", json=data[i])
    print(response.json())
print("-----------------------------------------------------------------------")
print()

"""
print("Getting all areas")
response = requests.get(BASE + "area")
print(response.json())
"""

"""
print("Update")
response = requests.patch(BASE + "person/2", {"first_name": "Paul"})
print(response.json())

response = requests.patch(BASE + "person/2", {"first_name": "Paul", "last_name": "Enriquez"})
print(response.json())



print("Delete")
response = requests.delete(BASE + "person/2")
print(response)
response = requests.delete(BASE + "person/2")
print(response)
response = requests.delete(BASE + "person/200")
print(response)
"""
