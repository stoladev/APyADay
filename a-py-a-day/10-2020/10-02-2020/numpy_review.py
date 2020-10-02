"""
Generally, NumPy arrays are more efficient than lists. One reason is that they allow you to do element-wise operations.
An element-wise operation allows you to quickly perform an operation, such as addition, on each element in an array.

Let’s compare how to add a number to each value in a python list versus a NumPy array:

# With a list
l = [1, 2, 3, 4, 5]
l_plus_3 = []
for i in range(len(l)):
    l_plus_3.append(l[i] + 3)
# With an array
a = np.array(l)
a_plus_3 = a + 3

As we can see, if we were to add 3 to every number in a list, we would have to use a for loop or a list comprehension.
With an array, we can just add 3. The same is true for subtraction, multiplication, and division.

We can also use NumPy Arrays to find the squares or square roots of each value.

Squaring each value:

>>> a ** 2
array([ 1,  4,  9, 16, 25, 36])
(Note: ** is the exponent notation in Python. For example, 3 squared can be calculated using 3 ** 2.)

Taking the square root of each value:

>>> np.sqrt(a)
array([ 1, 1.41421356, 1.73205081, 2, 2.23606798, 2.44948974])

"""

import numpy as np

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])

test_3_fixed = []
for i in range(len(test_3)):
    test_3_fixed.append(test_3[i] +2)

# The student’s grades on the third test are stored in the array test_3.
# But it turns out that one of the questions on the third test had an error. Give each student two extra points and
# save the new array to test_3_fixed.

"""
Operations with NumPy Arrays II
Arrays can also be added to or subtracted from each other in NumPy, assuming the arrays have the same number of
elements.

When adding or subtracting arrays in NumPy, each element will be added/subtracted to its matching element.

>>> a = np.array([1, 2, 3, 4, 5])
>>> b = np.array([6, 7, 8, 9, 10])
>>> a + b
array([ 7,  9, 11, 13, 15])

"""

# Let’s find the average of each student’s test scores to calculate their final grade for the semester. Start by adding
# the three arrays together and save the answer to the variable total_grade. Remember to use the fixed scores for
# test three.

# Now, divide total_grade by the number of tests taken to find the average score for each student. Save the answer to
# the variable final_grade.

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

total_grade = test_1 + test_2 + test_3_fixed

final_grade = total_grade / 3

print(final_grade)
