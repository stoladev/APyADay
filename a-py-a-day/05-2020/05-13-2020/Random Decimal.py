import random
from decimal import Decimal

# Creating a random decimal with 2 decimal places
def random_decimal():
    print(round(random.uniform(1.00, 1000.00), 2))

random_decimal()
