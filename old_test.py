import requests

BASE = "http://127.0.0.1:5000/"

print("Insert")
data = [
    {"first_name": "Juan", "last_name": "Perez", "age": 20},
    {"first_name": "Frida", "last_name": "Lopez", "age": 21},
    {"first_name": "Sebastian", "last_name": "Ruiz", "age": 22},
    {"first_name": "Beatriz", "last_name": "Sandoval", "age": 23},
    {"first_name": "Jaide", "last_name": "Martinez", "age": 24}
]

for i in range(len(data)):
    response = requests.post(BASE + "person/" + str(i), data[i])
    print(response.json())

print("Get")
response = requests.get(BASE + "person/1")
print(response.json())

response = requests.get(BASE + "person/200")
print(response.json())

response = requests.get(BASE + "person/2")
print(response.json())

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
