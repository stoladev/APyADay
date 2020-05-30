"""
Translating Python objects to JSON

This is the last lesson regarding files for a while.

Lessons learned:
- Open up file objects using open() and with.
- Read a file’s full contents using Python’s .read() method.
- Read a file line-by-line using .readline() and .readlines()
- Create new files by opening them in write-mode.
- Append to a file non-destructively by opening a file in append-mode.

Question:
What does the with command do in Python?
Answer:
Creates a context-manager, which performs cleanup after exiting the
adjacent indented block.
"""

import json

data_payload = [{
    'interesting message':
    'What is JSON? A web application\'s little pile of secrets.',
    'follow up': 'But enough talk!'
}]

with open('data.json', 'w') as data_json:
    json.dump(data_payload, data_json)

