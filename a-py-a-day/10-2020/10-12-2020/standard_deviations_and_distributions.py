"""
We know that the standard deviation affects the “shape” of our normal distribution. The last
exercise helps to give us a more quantitative understanding of this.

Suppose that we have a normal distribution with a mean of 50 and a standard deviation of 10. When
we say “within one standard deviation of the mean”, this is what we are saying mathematically:

lower_bound = mean - std
            = 50 - 10
            = 40

upper_bound = mean + std
            = 50 + 10
            = 60
It turns out that we can expect about 68% of our dataset to be between 40 and 60, for this
distribution.

As we saw in the previous exercise, no matter what mean and standard deviation we choose, 68% of
our samples will fall between +/- 1 standard deviation of the mean!

In fact, here are a few more helpful rules for normal distributions:

68% of our samples will fall between +/- 1 standard deviation of the mean
95% of our samples will fall between +/- 2 standard deviations of the mean
99.7% of our samples will fall between +/- 3 standard deviations of the mean

"""

# The average score on the SATs is 1000 and the standard deviation is 100.

# Calculate the amount that would be one standard deviation above the mean, and save it to the
# variable one_above.

# Calculate the amount that would be one standard deviation below the mean, and save it to the
# variable one_below.

# 2000 students took the exam. How many would you expect to have scores within the range of
# one_above and one_below?

one_above = 1000 + 100

one_below = 1000 - 100

print(one_above)

print(one_below)

one_std = 1360

print(one_std)
