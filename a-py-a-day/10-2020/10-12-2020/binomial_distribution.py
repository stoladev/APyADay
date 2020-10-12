"""
It’s known that a certain basketball player makes 30% of his free throws. On Friday night’s game,
he had the chance to shoot 10 free throws. How many free throws might you expect him to make? We
would expect 0.30 * 10 = 3.

However, he actually made 4 free throws out of 10 or 40%. Is this surprising? Does this mean that
he’s actually better than we thought?

The binomial distribution can help us. It tells us how likely it is for a certain number of
“successes” to happen, given a probability of success and a number of trials.

In this example:

The probability of success was 30% (he makes 30% of free throws)
The number of trials was 10 (he took 10 shots)
The number of successes was 4 (he made 4 shots)

The binomial distribution is important because it allows us to know how likely a certain outcome is,
even when it’s not the expected one. From this graph, we can see that it’s not that unlikely an
outcome for our basketball player to get 4 free throws out of 10. However, it would be pretty
unlikely for him to get all 10.

There are some complicated formulas for determining these types of probabilities. Luckily for us,
we can use NumPy - specifically, its ability to generate random numbers. We can use these random
numbers to model a distribution of numerical data that matches the real-life scenario we’re
interested in understanding.

For instance, suppose we want to know the different probabilities of our basketball player making
1, 2, 3, etc. out of 10 shots.

NumPy has a function for generating binomial distributions: np.random.binomial, which we can use to
determine the probability of different outcomes.

The function will return the number of successes for each “experiment”.

It takes the following arguments:

N: The number of samples or trials
P: The probability of success
size: The number of experiments
Let’s generate a bunch of “experiments” of our basketball player making 10 shots. We choose a big
N to be sure that our probabilities converge on the correct answer.

# Let's generate 10,000 "experiments"
# N = 10 shots
# P = 0.30 (30% he'll get a free throw)

a = np.random.binomial(10, 0.30, size=10000)
Now we have a record of 10,000 experiments. We can use Matplotlib to plot the results of all of
these experiments:

plt.hist(a, range=(0, 10), bins=10, normed=True)
plt.xlabel('Number of "Free Throws"')
plt.ylabel('Frequency')
plt.show()

"""

import numpy as np
from matplotlib import pyplot as plt

# A person sends 500 emails asking people to donate to their cause, with an estimated probability
# that 25 people (5%) will open the email and click to donate. There were 10,000 experiments.

# Using the binomial distribution formula, calculate the distribution and save it to the variable
# emails.

emails = np.random.binomial(500, 0.05, size=10000)

plt.hist(emails)

plt.show()

"""
Let’s return to our original question:

Our basketball player has a 30% chance of making any individual basket. He took 10 shots and made
4 of them, even though we only expected him to make 3. What percent chance did he have of making
those 4 shots?

We can calculate a different probability by counting the percent of experiments with the same
outcome, using the np.mean function.

Remember that taking the mean of a logical statement will give us the percent of values that
satisfy our logical statement.

Let’s calculate the probability that he makes 4 baskets:

a = np.random.binomial(10, 0.30, size=10000)
np.mean(a == 4)
When we run this code, we might get:

>> 0.1973
Remember, because we’re using a random number generator, we’ll get a slightly different result each
time. With the large *size we chose, the calculated probability should be accurate to about 2
decimal places.*

So, our basketball player has a roughly 20% chance of making 4 baskets.

This suggests that what we observed wasn’t that unlikely. It’s quite possible that he hasn’t got
any better; he just got lucky.

"""

# Let’s return to our email example. Remember that we sent 500 emails, with an estimated
# probability that 25 people would open the email. There were 10,000 trials.
# What is the probability that no one opens the email? Save the results to the variable no_emails.

# You recently hired a new marketing associate who wants to A/B test two emails to see if people
# respond better. What’s the probability that 8% or more of people will open the email? Save the
# results to the variable b_test_emails.

emails = np.random.binomial(500, 0.05, size=10000)

no_emails = np.mean(emails == 0)

b_test_emails = np.mean(emails >= 40)

print(no_emails)

print(b_test_emails)

# Practice what you’ve just learned with a dataset on sunflower heights! Imagine that you work for
# a botanical garden and you want to see how the sunflowers you planted last year did to see if you
# want to plant more of them.
# Calculate the mean and standard deviation of this dataset. Save the mean to sunflowers_mean and
# the standard deviation to sunflowers_std.

# We can see from the histogram that our data isn’t normally distributed. Let’s create a normally
# distributed sample to compare against what we observed.
#
# Generate 5,000 random samples with the same mean and standard deviation as sunflowers. Save
# these to sunflowers_normal.

# Now that you generated sunflowers_normal, uncomment (remove all of the #) the second plt.hist
# statement. Press run to see your normal distribution and your observed distribution.
# Generally, 10% of sunflowers that are planted fail to bloom. We planted 200, and want to know
# the probability that fewer than 20 will fail to bloom.

# First, generate 5,000 binomial random numbers that represent our situation. Save them to
# experiments.

# What percent of experiments had fewer than 20 sunflowers fail to bloom?
#
# Save your answer to the variable prob. This is the approximate probability that fewer than 20
# of our sunflowers will fail to bloom.

sunflowers = np.genfromtxt('sunflower_heights.csv',
                           delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# Calculate sunflowers_normal here:
sunflowers_normal = np.random.normal(
  loc=sunflowers_mean,
  scale=sunflowers_std,
  size=5000
)

plt.hist(sunflowers,
         range=(11, 15), histtype='step', linewidth=2,
        label='Observed', normed=True)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='Normal', normed=True)
plt.legend()
plt.show()


# Calculate probabilities here:
experiments = np.random.binomial(200, 0.1, size=5000)
prob = np.mean(experiments < 20)
print(prob)
