"""
Selecting elements from a 2-d array is very similar to selecting them from a 1-d array, we just
have two indices to select from. The syntax for selecting from a 2-d array is a[row,column] where
a is the array.

It’s important to note that when we work with arrays that have more than one dimension, the
relationship between the interior arrays is defined in terms of axes. A two-dimensional array has
two axes: axis 0 represents the values that share the same indexical position (are in the same
column), and axis 1 represents the values that share an array (are in the same row). This is
illustrated below.

Consider the array

a = np.array([[32, 15, 6, 9, 14],
              [12, 10, 5, 23, 1],
              [2, 16, 13, 40, 37]])
We can select specific elements using their indices:

a[2,1]
16
Let’s say we wanted to select an entire column, we can insert : as the row index:

# selects the first column
a[:,0]
array([32, 12,  2])
The same works if we want to select an entire row:

# selects the second row
a[1,:]
array([12, 10,  5, 23,  1])
We can further narrow it down and select a range from a specific row:

# selects the first three elements of the first row
a[0,0:3]
array([32, 15,  6])

"""

