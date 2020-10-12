"""
In a dataset, the median value can provide an important comparison to the mean. Unlike a mean, the median is not
affected by outliers. This becomes important in skewed datasets, datasets whose values are not distributed evenly.
Let’s write a program that explores this idea further.

"""

import numpy as np

time_spent = np.genfromtxt('file.csv', delimiter=',')

print(time_spent)

# Find the average amount of time in minutes spent on the website and save it to the variable minutes_mean.

minutes_mean = time_spent.mean()

# Now, find the median of the array and save it to the variable minutes_median.

minutes_median = np.median(time_spent)

"""
As we know, the median is the middle of a dataset: it is the number for which 50% of the samples are below, and 50% of
the samples are above. But what if we wanted to find a point at which 40% of the samples are below, and 60% of the
samples are above?

This type of point is called a percentile. The Nth percentile is defined as the point N% of samples lie below it. So
the point where 40% of samples are below is called the 40th percentile. Percentiles are useful measurements because
they can tell us where a particular value is situated within the greater dataset.

Let’s look at the following array:

d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
There are 11 numbers in the dataset. The 40th percentile will have 40% of the 10 remaining numbers below it (40% of 10
is 4) and 60% of the numbers above it (60% of 10 is 6). So in this example, the 40th percentile is 4.

In NumPy, we can calculate percentiles using the function np.percentile, which takes two arguments: the array and the
percentile to calculate.

Here’s how we would use NumPy to calculate the 40th percentile of array d:

>>> d = np.array([1, 2, 3, 4, 4, 4, 6, 6, 7,  8, 8])
>>> np.percentile(d, 40)
4.00

"""

# The local public library wants to study how many hours a week their patrons use the computers. At the top of the
# script.py, we have included sample data from 11 users in a NumPy array.
# Use NumPy to find the 30th percentile of the sorted array and save it to a variable named thirtieth_percentile.

patrons = np.array([2, 6, 14, 4, 3, 9, 1, 11, 4, 2, 8])

thirtieth_percentile = np.percentile(patrons, 30)

"""
ome percentiles have specific names:

The 25th percentile is called the first quartile
The 50th percentile is called the median
The 75th percentile is called the third quartile
The minimum, first quartile, median, third quartile, and maximum of a dataset are called a five-number summary. This
set of numbers is a great thing to compute when we get a new dataset.

The difference between the first and third quartile is a value called the interquartile range. For example, say we
have the following array:

d = [1, 2, 3, 4, 4, 4, 6, 6, 7, 8, 8]
We can calculate the 25th and 75th percentiles using np.percentile:

np.percentile(d, 25)
>>> 3.5
np.percentile(d, 75)
>>> 6.5
Then to find the interquartile range, we subtract the value of the 25th percentile from the value of the 75th:

6.5 - 3.5 = 3
50% of the dataset will lie within the interquartile range. The interquartile range gives us an idea of how spread out
our data is. The smaller the interquartile range value, the less variance in our dataset. The greater the value,
the larger the variance.

"""

# An online movie streaming company wants to know how many movies users watch in one week. At the top of the script.py,
# we have included sample data from 15 users in an array.
# Find the 25th and 75th percentiles, and save them to the corresponding variables: first_quarter and third_quarter.

movies_watched = np.array([2, 3, 8, 0, 2, 4, 3, 1, 1, 0, 5, 1, 1, 7, 2])

first_quarter = np.percentile(movies_watched, 25)
third_quarter = np.percentile(movies_watched, 75)

# Create a variable named interquartile_range. Calculate the interquartile range and save it to this variable.

interquartile_range = third_quarter - first_quarter
print(first_quarter)
print(third_quarter)
print(interquartile_range)

# We can find the standard deviation of a dataset using the Numpy function np.std:
# >>> nums = np.array([65, 36, 52, 91, 63, 79])
# >>> np.std(nums)
# 17.716909687891082

# You’ve been asked to judge your town’s annual squash festival. The festival organizer gives you a list that includes
# all the weights for the two competitions that you’re judging: pumpkins and acorn squash.
# Given the two data sets at the top of script.py, find the average weight for each competition and save them to the
# variables pumpkin_avg and acorn_squash_avg.

pumpkin = np.array([68, 1820, 1420, 2062, 704, 1156, 1857, 1755, 2092, 1384])

acorn_squash = np.array([20, 43, 99, 200, 12, 250, 58, 120, 230, 215])

pumpkin_avg = np.mean(pumpkin)

acorn_squash_avg = np.mean(acorn_squash)

# Now, the rest of the judges want you to give them an idea of how representative the mean values are in relation to
# the entirety of the submissions. Calculate the standard deviation for each of the datasets to find and save them to
# the variables pumpkin_std and acorn_squash_std.

pumpkin_std = np.std(pumpkin)

acorn_squash_std = np.std(acorn_squash)

# A group of citizen scientists has been collecting data on rainfall in Seattle. They’ve presented their data to you
# in the form of monthly averages, measured in inches.
# Month	Avg. Precipitation
# January	5.21
# February	3.76
# March	3.27
# April	2.35
# May	1.89
# June	1.55
# July	0.65
# August	1.06
# September	1.72
# October	3.36
# November	4.82
# December	5.11
# We’ve saved this data to the NumPy array rainfall.

rainfall = np.array([5.21, 3.76, 3.27, 2.35, 1.89, 1.55, 0.65, 1.06, 1.72, 3.35, 4.82, 5.11])

# Find the mean of the rainfall array and save it to the variable rain_mean.

rain_mean = np.mean(rainfall)

# Find the median of the rainfall array and save it to the variable rain_median.

rain_median = np.median(rainfall)

# Find the 25th and the 75th percentiles of the original rainfall array and save them to the arrays first_quarter and
# third_quarter, respectively.

first_quarter = np.percentile(rainfall, 25)

third_quarter = np.percentile(rainfall, 75)

# Calculate the interquartile range and save it to the variable, interquartile_range.

interquartile_range = third_quarter - first_quarter

# Determine the standard deviation of the set and save it to the variable rain_std.

rain_std = np.std(rainfall)