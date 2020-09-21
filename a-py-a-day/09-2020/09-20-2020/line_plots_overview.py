"""
Matplotlib will automatically place the two lines on the same axes and give them different colors if you call
plt.plot() twice.

Let’s look at the graph we made in the last exercise to track lunch spending, where days is on the x-axis and spending
(money_spent) is on the y-axis:

money_spent

We could add a friend’s lunch spending for comparison like this:

# Days of the week:
days = [0, 1, 2, 3, 4, 5, 6]
# Your Money:
money_spent = [10, 12, 12, 10, 14, 22, 24]
# Your Friend's Money:
money_spent_2 = [11, 14, 15, 15, 22, 21, 12]
# Plot your money:
plt.plot(days, money_spent)
# Plot your friend's money:
plt.plot(days, money_spent_2)
# Display the result:
plt.show()

We then get two lines on the same plot:

money_spent_2

By default, the first line is always blue, and the second line is always orange. In the next exercise, we’ll learn how
to customize these lines ourselves.
"""

# We have defined lists called time, revenue, and costs. Plot revenue vs time.

from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue)
plt.plot(time, costs)

plt.show()
