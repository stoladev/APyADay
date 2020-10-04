"""
Two-Dimensional Arrays
In Python, we can create lists that are made up of other lists. Similarly, in NumPy we can create an array of arrays. If the arrays that make up our bigger array are all the same size, then it has a special name: a two-dimensional array.

In the previous exercises we had stored the students’ test scores in separate one-dimensional arrays for each test:

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
But we could have also stored all of this data in a single, two-dimensional array:

np.array([[92, 94, 88, 91, 87], 
          [79, 100, 86, 93, 91],
          [87, 85, 72, 90, 92]])
Here, each row represents a test, and each column represents a student. This allows us to store all of our data in a single array without losing any of its organization.

As we mentioned, a two-dimensional array is a list of lists where each list has the same number of elements. Here are some examples that are not two-dimensional arrays.

This code will run but it will not create a two-dimensional array because the lists have different numbers of elements:

np.array([[29, 49,  6], 
          [77,  1]])
This code will not run because the [] for the outer lists are missing:

np.array([68, 16, 73],
         [61, 79, 30])

"""

# In statistics, we often use two-dimensional arrays to represent a set of samples. For instance,
# if we flip a coin we can represent each head as a 1 and each tail as a 0.

# Create a one-dimensional array for a coin toss experiment that results in heads, tails, tails,
# heads, tails, and save it to the variable coin_toss.

import numpy as np

coin_toss = np.array([1, 0, 0, 1, 0])

coin_toss_again = np.array([[1, 0, 0, 1, 0], [0, 0, 1, 1, 1]])

