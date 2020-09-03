"""
Applying a Lambda to a Column

In Pandas, we often use lambda functions to perform complex operations on columns. For example,
suppose that we want to create a column containing the email provider for each email address in the
following table:

Name    Email
JOHN SMITH  john.smith@gmail.com
Jane Doe    jdoe@yahoo.com
joe schmo   joeschmo@hotmail.com

We could use the following code with a lambda function and the string method .split():

df['Email Provider'] = df.Email.apply(lambda x: x.split('@')[-1])

The result would be:

Name    Email   Email Provider
JOHN SMITH  john.smith@gmail.com    gmail.com
Jane Doe    jdoe@yahoo.com  yahoo.com
joe schmo   joeschmo@hotmail.com    hotmail.com

"""

# Create a lambda function get_last_name which takes a string with someone’s first and last name
# (i.e., John Smith), and returns just the last name (i.e., Smith).

import pandas as pd

df = pd.read_csv("employees.csv")

get_last_name = lambda x: x.split()[-1]
df["last_name"] = df.name.apply(get_last_name)

print(df)

