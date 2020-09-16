"""

This type of merge (where we only include matching rows) is called an inner merge. There are other types of merges that
we can use when we want to keep information from the unmatched rows.

Suppose that two companies, Company A and Company B have just merged. They each have a list of customers, but they keep
slightly different data. Company A has each customer’s name and email. Company B has each customer’s name and phone
number. They have some customers in common, but some are different.

company_a
name 	email
Sally Sparrow 	sally.sparrow@gmail.com
Peter Grant 	pgrant@yahoo.com
Leslie May 	leslie_may@gmail.com

company_b
name 	phone
Peter Grant 	212-345-6789
Leslie May 	626-987-6543
Aaron Burr 	303-456-7891

If we wanted to combine the data from both companies without losing the customers who are missing from one of the
tables, we could use an Outer Join. An Outer Join would include all rows from both tables, even if they don’t match.
Any missing values are filled in with None or nan (which stands for “Not a Number”).

pd.merge(company_a, company_b, how='outer')

The resulting table would look like this:
name 	email 	phone
Sally Sparrow 	sally.sparrow@gmail.com 	nan
Peter Grant 	pgrant@yahoo.com 	212-345-6789
Leslie May 	leslie_may@gmail.com 	626-987-6543
Aaron Burr 	nan 	303-456-7891

"""

# There are two hardware stores in town: Store A and Store B. Store A’s inventory is in DataFrame store_a and Store B’s
# inventory is in DataFrame store_b. They have decided to merge into one big Super Store!
# Combine the inventories of Store A and Store B using an outer merge. Save the results to the variable store_a_b_outer.

import pandas as pd

store_a = pd.read_csv('store_a.csv')
print(store_a)
store_b = pd.read_csv('store_b.csv')
print(store_b)

store_a_b_outer = pd.merge(store_a, store_b, how='outer')
