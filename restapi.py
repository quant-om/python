# XML : eXtended Markup Language
"""
<student>
    <id>1234</id>
    <name>quant-om</name>
</student>
"""
# JSON : Java Script Object Notation
# This is similar to Python dictionaries
"""
{ }

{
    "name": "quant-om",
    "id": 1.0,
    "values": [ "123", "234", "345" ],
    "myd": { "name": [7, 9 , 0, [9, 7]] }
}
"""

import requests
print("Demonstrating rest/api in Python.")
# We have to use 'requests' module

# Using GET http method.
resp = requests.get("https://jsonplaceholder.typicode.com/todos")
print(f"Response CODE is {resp}")
# Requirement : To print all titles when completed is false.
resp_json = resp.json()

for val in resp_json:
    if val['completed'] is False:
        print(f"title: {val['title']}")

# Try completed is True
# Try only when userid is 1, and print all values one by one
# Try when id is less 25, and print all values.


