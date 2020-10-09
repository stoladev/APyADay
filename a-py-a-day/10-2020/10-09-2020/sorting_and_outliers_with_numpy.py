"""
Sorting and Outliers
One way to quickly identify outliers is by sorting our data, Once our data is sorted, we can
quickly glance at the beginning or end of an array to see if some values lie far beyond the
expected range. We can use the NumPy function np.sort to sort our data.

Let’s go back to our 3rd grade height example, and imagine an 8th grader walked into our
experiement:

>>> heights = np.array([49.7, 46.9, 62, 47.2, 47, 48.3, 48.7])

If we use np.sort, we can immediately identify the taller student since their height (62”) is
noticeably outside the range of the dataset:

>>> np.sort(heights)
array([ 46.9,  47. ,  47.2,  48.3,  48.7,  49.7,  62])

"""


import numpy as np

temps = np.array(
    [
        86,
        88,
        94,
        85,
        97,
        90,
        87,
        85,
        94,
        93,
        92,
        95,
        98,
        85,
        94,
        91,
        97,
        88,
        87,
        86,
        99,
        89,
        89,
        99,
        88,
        96,
        93,
        96,
        85,
        88,
        191,
        95,
        96,
        87,
        99,
        93,
        90,
        86,
        87,
        100,
        187,
        98,
        101,
        101,
        96,
        94,
        96,
        87,
        86,
        92,
        98,
        94,
        98,
        90,
        99,
        96,
        99,
        86,
        97,
        98,
        86,
        90,
        86,
        94,
        91,
        88,
        196,
        195,
        93,
        97,
        199,
        87,
        87,
        90,
        90,
        98,
        88,
        92,
        97,
        88,
        85,
        94,
        88,
        93,
        198,
        90,
        91,
        90,
        92,
        92,
    ]
)

# You’ve been tracking temperature data over the summer on your back porch, but realized that you
# placed your sensor right over a grill! Before you can use your data, you need to check to see if
# the heat from the grill caused any weird readings that could skew your data.

# First, sort the temps data array and save the sorted data to a sorted_temps variable.

sorted_temps = np.sort(temps)

# Now, print the sorted_temps array. What do we see? Did the grill, in fact, create outliers in
# our data?

print(sorted_temps)

"""
Another key metric that we can use in data analysis is the median. The median is the middle value
of a dataset that’s been ordered in terms of magnitude (from lowest to highest).

Let’s look at the following array:

np.array( [1, 1, 2, 3, 4, 5, 5])
In this example, the median would be 3, because it is positioned half-way between the minimum
value and the maximum value.

If the length of our dataset was an even number, the median would be the value halfway between the
two central values. So in the following example, the median would be 3.5:

np.array( [1, 1, 2, 3, 4, 5, 5, 6])
But what if we had a very large dataset? It would get very tedious to count all of the values.
Luckily, NumPy also has a function to calculate the median, np.median:

>>> my_array = np.array([50, 38, 291, 59, 14])
>>> np.median(my_array)
50.0

"""

# You’re doing some research on household incomes and come across the following small dataset:

# 10100, 35500, 105000, 85000, 25500, 40500, 65000
# Calculate the median, without using Numpy, and save the value to the variable small_set_median.


large_set = np.genfromtxt("household_income.csv", delimiter=",")

small_set_median = 40500

# As you continue your research, you come across a trove of research in the file household_income.csv, which we’ve
# already included in your program and saved as large_set.
# Use NumPy to find the median of large_set and save the result to the variable large_set_median.

large_set_median = np.median(large_set)
