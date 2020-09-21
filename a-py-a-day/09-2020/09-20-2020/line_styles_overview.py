"""
We can specify a different color for a line by using the keyword color with either an HTML color name or a HEX code:

plt.plot(days, money_spent, color='green')
plt.plot(days, money_spent_2, color='#AAAAAA')

money_colors

We can also make a line dotted or dashed using the keyword linestyle.

# Dashed:
plt.plot(x_values, y_values, linestyle='--')
# Dotted:
plt.plot(x_values, y_values, linestyle=':')
# No line:
plt.plot(x_values, y_values, linestyle='')

We can also add a marker using the keyword marker:

# A circle:
plt.plot(x_values, y_values, marker='o')
# A square:
plt.plot(x_values, y_values, marker='s')
# A star:
plt.plot(x_values, y_values, marker='*')

To see all of the possible options, check out the Matplotlib documentation. Here are a couple of those values applied
to our plots about lunch spending:

plt.plot(days, money_spent, color='green', linestyle='--')
plt.plot(days, money_spent_2, color='#AAAAAA',  marker='o')

linestyles

Let’s get some practice with customizing lines on the same plot.
Instructions
"""

# Plot revenue vs. time as a purple ('purple'), dashed ('--') line.

import matplotlib.pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(time, revenue, color='purple', linestyle='--')
plt.plot()

plt.plot(time, costs, color='#82edc9', marker='s')
plt.plot()

plt.show()
