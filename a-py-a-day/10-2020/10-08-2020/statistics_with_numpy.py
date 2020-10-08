"""
The first statistical concept we’ll explore is mean, also commonly referred to as an average. The
mean is a useful measurement to get the center of a dataset. NumPy has a built-in function to
calculate the average or mean of arrays: np.mean

Let’s say we want to find the average number of pounds of produce a person purchases per week. We
administered a survey and received 1,000 responses:

survey_responses = [5, 10.2, 4, .3 ... 6.6]
We can then transform the dataset into a NumPy array and use the function np.mean to calculate the
average:

survey_array = np.array(survey_responses)
np.mean(survey_array)
5.220

"""

# The beverage distributor, Wine Not? wants to calculate how many bottles of Bourdeaux it sells on
# average at three area wine sellers to determine whether or not it should increase its stock. The
# sales for the past week for each store are listed in script.py.

# Find the average sales for each store, and save them to the variables store_one_avg,
# store_two_avg, and store_three_avg.


import numpy as np

store_one = np.array([2, 5, 8, 3, 4, 10, 15, 5])
store_two = np.array([3, 17, 18, 9, 2, 14, 10])
store_three = np.array([7, 5, 4, 3, 2, 7, 7])

store_one_avg = np.mean(store_one)
store_two_avg = np.mean(store_two)
store_three_avg = np.mean(store_three)


# Notice the average sales per week for each store. The boss says that we should increase what we
# stock, but only if the store’s average sales are greater than 7 bottles per week.

# Save the store dataset variable name that fits this description to the variable best_seller.

best_seller = store_two


# You’re running an alumni reunion at your local college. You have a list of the names of each
# person in attendance and the year that they graduated.

# We’ve saved this list as a NumPy array to the variable class_year. Calculate the percent of
# attending alumni who graduated on and after 2005 and save your result to the variable
# millennials.

class_year = np.array(
    [
        1967,
        1949,
        2004,
        1997,
        1953,
        1950,
        1958,
        1974,
        1987,
        2006,
        2013,
        1978,
        1951,
        1998,
        1996,
        1952,
        2005,
        2007,
        2003,
        1955,
        1963,
        1978,
        2001,
        2012,
        2014,
        1948,
        1970,
        2011,
        1962,
        1966,
        1978,
        1988,
        2006,
        1971,
        1994,
        1978,
        1977,
        1960,
        2008,
        1965,
        1990,
        2011,
        1962,
        1995,
        2004,
        1991,
        1952,
        2013,
        1983,
        1955,
        1957,
        1947,
        1994,
        1978,
        1957,
        2016,
        1969,
        1996,
        1958,
        1994,
        1958,
        2008,
        1988,
        1977,
        1991,
        1997,
        2009,
        1976,
        1999,
        1975,
        1949,
        1985,
        2001,
        1952,
        1953,
        1949,
        2015,
        2006,
        1996,
        2015,
        2009,
        1949,
        2004,
        2010,
        2011,
        2001,
        1998,
        1967,
        1994,
        1966,
        1994,
        1986,
        1963,
        1954,
        1963,
        1987,
        1992,
        2008,
        1979,
        1987,
    ]
)

millennials = np.mean(class_year > 2004)

"""
If we have a two-dimensional array, np.mean can calculate the means of the larger array as well as
the interior values.

Let’s imagine a game of ring toss at a carnival. In this game, you have three different chances to
get all three rings onto a stick. In our ring_toss array, each interior array (the arrays within
the larger array) is one try, and each number is one ring toss. 1 represents a successful toss, 0
represents a fail.

First, we can use np.mean to find the mean across all the arrays:

ring_toss = np.array([[1, 0, 0],
                          [0, 0, 1],
                          [1, 0, 1]])
np.mean(ring_toss)
0.44444444444444442
To find the means of each interior array, we specify axis 1 (the “rows”):

np.mean(ring_toss, axis=1)
array([ 0.33333333,  0.33333333,  0.66666667])
To find the means of each index position (i.e, mean of all 1st tosses, mean of all 2nd tosses, …),
we specify axis 0 (the “columns”):

np.mean(ring_toss, axis=0)
array([ 0.66666667,  0.        ,  0.66666667])

"""

# In script.py, we’ve provided data about a trial for a new allergy medication, AllerGeeThatSucks!
# Five participants were asked to rate how drowsy the medication made them once a day for three
# days on a scale of one (least drowsy) to ten (most drowsy).

# Use np.mean to find the average level of drowsiness across all the trials and save the result to
# the variable total_mean.

allergy_trials = np.array([[6, 1, 3, 8, 2], [2, 6, 3, 9, 8], [5, 2, 6, 9, 9]])

total_mean = np.mean(allergy_trials)

# Use np.mean to find the average level of drowsiness across each day of the experiment and save
# to the variable trial_mean.

trial_mean = np.mean(allergy_trials, axis=1)

# Use np.mean to find the average level of drowsiness across for each individual patient to see if
# some were more sensitive to the drug than others and save it to the variable patient_mean.

patient_mean = np.mean(allergy_trials, axis=0)
