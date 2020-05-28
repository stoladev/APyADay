"""
JavaScript Object Notation. Similar to python's dictionary syntax.
"""

# Suppose we have a file like the following:

"""
{
    'user': 'ellen_greg',
    'action': 'purchase',
    'item_id': '14781239',
}
"""

# To read that:

import json

with open('purchase_14781239.json') as purchase_json:
    purchase_data = json.load(purchase_json)

print(purchase_data['user'])
# This prints 'ellen_greg'


