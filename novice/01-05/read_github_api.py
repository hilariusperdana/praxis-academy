import json
from urllib import request

url="https://api.github.com/users/hilariusperdana"
response = request.urlopen(url)
data=json.loads(response.read())
print("== program baca github ==")
print(f"Nama: {data['name]}")