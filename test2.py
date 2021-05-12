import requests

#BASE = 'http://localhost:5000/'
BASE = 'https://www.apielectoral.mx/'
BASE = 'https://e7f1hlosbh.execute-api.us-east-2.amazonaws.com/staging/'

auth_header = {
	'Authorization': 'eyJraWQiOiJQNU9BRVwvbWwwUTdHRko0WVl0aVp6c3ZiXC9QU1JhXC9pbFZiOUNCeVdDSFpRPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoicGpsbm5XSzVrcUp5LUttYndQRjRXUSIsInN1YiI6ImU3ZmE4MDRiLTdkYmEtNDdlMy1iNDQ0LTIzMWFmMDg5YmRiMCIsImF1ZCI6IjZkYjZibGxsYWltMWVicW5lZm9lNjFibjlsIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjIwNzg5ODE3LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9KMUtJc2NwaGgiLCJjb2duaXRvOnVzZXJuYW1lIjoiZTdmYTgwNGItN2RiYS00N2UzLWI0NDQtMjMxYWYwODliZGIwIiwiZXhwIjoxNjIwODA0MjE3LCJpYXQiOjE2MjA3ODk4MTgsImVtYWlsIjoicGF1bC5hZ3VpbGFyQHNvY2lhbHRpYy5vcmcifQ.DRdnTO_b0a9mD8NbbiAvhH94cpofe1t6uqCRN4hNuFlotHXalgXHjxRUrvnkgJq90yRyIuKysNwzewxdY7RMOTcrw93cBfFfj8LiMbCI2sWNDnEDh0UbvI1WFQRbKr96VdRQ-J1JLKEeKyonDn4aGLLCRU2c8t9nWQZEdWyXXrENVJc6Cvum-HqeBRpjBHfVzYzDQuLqSfu_WfKhJvo65IXwRR8lTDRgvGdy5P47g7szQrIQiXxEYAC-yLRB8V_wB21IWHngxBsj6Cay6y0iHMcwmbuqQjBe5VbJn7SIzN-isWyigtKyY1IwtvyteyJS2VsqIOQmf3Kjh5m8VL-Y1w'
}

print('-----------------------------------------------------------------------')
print('Getting areas')
response = requests.get(BASE + 'area', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting an area')
response = requests.get(BASE + 'area/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print('-----------------------------------------------------------------------')
print('Getting chambers')
response = requests.get(BASE + 'chamber', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting a chamber')
response = requests.get(BASE + 'chamber/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print('-----------------------------------------------------------------------')
print('Getting roles')
response = requests.get(BASE + 'role', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting a role')
response = requests.get(BASE + 'role/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print('-----------------------------------------------------------------------')
print('Getting coalitions')
response = requests.get(BASE + 'coalition', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting a coalition')
response = requests.get(BASE + 'coalition/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')


print('-----------------------------------------------------------------------')
print('Getting parties')
response = requests.get(BASE + 'party', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting a party')
response = requests.get(BASE + 'party/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print('-----------------------------------------------------------------------')
print('Getting persons')
response = requests.get(BASE + 'person', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting a person')
response = requests.get(BASE + 'person/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print('-----------------------------------------------------------------------')
print('Getting other names')
response = requests.get(BASE + 'other_name', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting an other name')
response = requests.get(BASE + 'other_name/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print('-----------------------------------------------------------------------')
print('Getting professions')
response = requests.get(BASE + 'profession', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting a profession')
response = requests.get(BASE + 'profession/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print('-----------------------------------------------------------------------')
print('Getting person professions')
response = requests.get(BASE + 'person-profession', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting a person profession')
response = requests.get(BASE + 'person-profession/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')


print('-----------------------------------------------------------------------')
print('Getting memberships')
response = requests.get(BASE + 'membership', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting a membership')
response = requests.get(BASE + 'membership/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print('-----------------------------------------------------------------------')
print('Getting contests')
response = requests.get(BASE + 'contest', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting a contest')
response = requests.get(BASE + 'contest/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print('-----------------------------------------------------------------------')
print('Getting urls')
response = requests.get(BASE + 'url', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('Getting an url')
response = requests.get(BASE + 'url/1', headers=auth_header, verify=True,  timeout=None)
print(response.json())
print('-----------------------------------------------------------------------')
input('Presiona enter para continuar')

print("¡YOU WIN!")

'''
requests.get
requests.post
requests.patch
requests.delete
'''
