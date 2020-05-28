"""
You can use the json library to translate Python objects to JSON as well. This
is useful when you are using a Python library to serve web pages - you'd also
be able to serve JSON.
"""
import json

# Let's say we had a python dictionary we wanted to save as a JSON file:

turn_to_json = {
    "eventId": 674189,
    "dateTime": "2015-02-12T09:23:17.511Z",
    "chocolate": "Semi-sweet Dark",
    "isTomatoAFruit": True,
}

# We'd be able to create a JSON file with that by doing the following:

with open('output.json', 'w') as json_file:
    json.dump(turn_to_json, json_file)

# We open up a write-mode file under json_file, use json.dump() to write.
# json.dump() takes two args: data object + file object you want to save.

data_payload = [{
    'interesting message':
    'What is JSON? A web application\'s little pile of secrets.',
    'follow up': 'But enough talk!'
}]
