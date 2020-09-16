"""

Suppose we want to identify which customers are missing phone information. We would want a list of all customers who
have email, but don’t have phone.

We could get this by performing a Left Merge. A Left Merge includes all rows from the first (left) table, but only rows
from the second (right) table that match the first table.

For this command, the order of the arguments matters. If the first DataFrame is company_a and we do a left join, we’ll
only end up with rows that appear in company_a.

By listing company_a first, we get all customers from Company A, and only customers from Company B who are also
customers of Company A.

pd.merge(company_a, company_b, how='left')

The result would look like this:
name 	email 	phone
Sally Sparrow 	sally.sparrow@gmail.com 	None
Peter Grant 	pgrant@yahoo.com 	212-345-6789
Leslie May 	leslie_may@gmail.com 	626-987-6543

Now let’s say we want a list of all customers who have phone but no email. We can do this by performing a Right Merge.

"""

# Let’s return to the two hardware stores, Store A and Store B. They’re not quite sure if they want to merge into a big
# Super Store just yet.
# Store A wants to find out what products they carry that Store B does not carry. Using a left merge, combine store_a
# to store_b and save the results to store_a_b_left.
# The items with null in store_b_inventory are carried by Store A, but not Store B.

import pandas as pd

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_left = pd.merge(store_a, store_b, how='left')

"""

Right merge is the exact opposite of left merge. Here, the merged table will include all rows from the second (right)
table, but only rows from the first (left) table that match the second table.

By listing company_a first and company_b second, we get all customers from Company B, and only customers from Company A
who are also customers of Company B.

pd.merge(company_a, company_b, how="right")

The result would look like this:
name 	email 	phone
Peter Grant 	pgrant@yahoo.com 	212-345-6789
Leslie May 	leslie_may@gmail.com 	626-987-6543
Aaron Burr 	None 	303-456-7891

"""

# Now, Store B wants to find out what products they carry that Store A does not carry. Use a left join, to combine the
# two DataFrames but in the reverse order (i.e., store_b followed by store_a) and save the results to the variable
# store_b_a_left.
# Which items are not carried by Store A, but are carried by Store B?

store_b_a_left = pd.merge(store_b, store_a, how='left')
