"""
Logical Operations with Arrays
Another useful thing that arrays can do is perform element-wise logical operations. For instance,
suppose we want to know how many elements in an array are greater than 5. We can easily write some
code that checks to see whether this statement evaluates to True for each item in the array,
without having to use a for loop :

a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
a > 5
array([True, False, False, False, False, False, True, True, True, True], dtype=bool)
We can then use logical operators to evaluate and select items based on certain criteria. To
select all elements from the previous array that are greater than 5, we’d write the following:

a[a > 5]
array([10, 9, 8, 9, 7])
We can also combine logical statements to further specify our criteria. To do so, we place each
statement in parentheses and use boolean operators like & (and) and | (or).

In our example, we can use combined statements to find the elements that are greater than five or
less than two:

a[(a > 5) | (a < 2)]
array([10, 9, 8, 9, 7])

"""

# Today we’re visiting the Goldilocks Porridge Festival, sampling a selection of breakfast
# cereals and judging them based on their temperature (listed in Fahrenheit).
# Create a logical condition that selects samples in the porridge array that are less than 60,
# and save them to a variable named cold.

# Create a logical condition that finds all the samples that are between 60 and 80 and save them
# to a variable named just_right.

# Print each array to the terminal.

import numpy as np

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]

hot = porridge[porridge > 80]

just_right = porridge[(porridge > 60) & (porridge < 80)]

print(cold)
print(hot)
print(just_right)
