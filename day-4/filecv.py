import json #json example #python to json
############ dictionary format
student = {"name": "Madhu","age": 20}

data = json.dumps(student)
print(data)

import json   # json to python    
json_data = '{"name": "Madhu", "age": 20}'       ##### sets format
python_data = json.loads(json_data)
print(type(python_data))

import requests

response = requests.get(
    "https://api.github.com/users/python"
)
data = response.json()
print(data)