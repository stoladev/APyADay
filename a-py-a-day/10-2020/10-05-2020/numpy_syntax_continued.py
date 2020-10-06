"""
Selecting Elements from a 1-D Array
NumPy allows us to select elements from an array using their indices. Consider the one-dimensional
array

a = np.array([5, 2, 7, 0, 11])
If we wanted to select the first element in this array, we would call:

a[0]
5

In typical Python fashion, the indices for an array start at 0. This is known as zero-indexed
numbering. In the array above, 5 is known as the zeroth element, a[0]. It follows that 2 is the
first element, a[1].

We can also select negative indices, which count from opposite end of the array and start at -1.
This is particularly useful when you want to access the last element or two of an array:

a[-1]
11
a[-2]
0

If we wanted to select multiple elements in the array, we can define a range, such as a[1:3],
which will select all the elements from a[1] to a[3], including a[1] but excluding a[3].

a[1:3]
array([2, 7])

Similarly, if we wanted to select all elements before a[3] we would use:

a[:3]
array([5, 2, 7])

We can also use negative indices to select multiple elements. Let’s say we want to select the last
3 elements in an array:

a[-3:]
array([7, 0, 11])

Notice that when we select multiple elements, we get an array.

"""

# Let’s return to our student’s test scores. The following table shows all three test arrays
# aligned to the names of the students.

# Tanya	Manual	Adwoa	Jeremy	Cody
# test_1	92	94	88	91	87
# test_2	79	100	86	93	91
# test_3	87	85	72	90	92

# Jeremy wants to know what he scored on the second test.
# Select the score from the test_2 array and save it to the variable jeremy_test_2.

# You want to compare how Manual and Adwoa did on the first test.
# Select both of their scores and save them in an array named manual_adwoa_test_1.

import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

jeremy_test_2 = test_2[3]

manual_adwoa_test_1 = test_1[1:3]
