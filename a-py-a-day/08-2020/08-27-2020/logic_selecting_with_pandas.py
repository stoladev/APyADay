"""

You can select a subset of a DataFrame by using logical statements:
df[df.MyColumnName == desired_column_value]

In Python, == is how we test if a value is exactly equal to another value.

We can use other logical statements, such as:

Greater Than, > — Here, we select all rows where the customer’s age is greater than 30:

    df[df.age > 30]

Less Than, < — Here, we select all rows where the customer’s age is less than 30:

    df[df.age < 30]

Not Equal, != — This snippet selects all rows where the customer’s name is not Clara Oswald:

    df[df.name != 'Clara Oswald']

"""

import pandas as pd

df = pd.DataFrame(
    [
        ["January", 100, 100, 23, 100],
        ["February", 51, 45, 145, 45],
        ["March", 81, 96, 65, 96],
        ["April", 80, 80, 54, 180],
        ["May", 51, 54, 54, 154],
        ["June", 112, 109, 79, 129],
    ],
    columns=["month", "clinic_east", "clinic_north", "clinic_south", "clinic_west"],
)

january = df[df.month == "January"]

"""
You can also combine multiple logical statements, as long as each statement is in parentheses.

For instance, suppose we wanted to select all rows where the customer’s age was under 30 or the
customer’s name was “Martha Jones”:

We could use the following code:

    df[(df.age < 30) |
        (df.name == 'Martha Jones')]

In Python, | means “or” and & means “and”.

"""

march_april = df[(df.month == "March") | (df.month == "April")]

"""

Suppose we want to select the rows where the customer’s name is either “Martha Jones”, “Rose Tyler”
or “Amy Pond”.

We could use the isin command to check that df.name is one of a list of values:

    df[df.name.isin(['Martha Jones',
        'Rose Tyler',
        'Amy Pond'])]

"""

january_february_march = df[df.month.isin(["January", "February", "March"])]

