"""
A lambda function is a way of defining a function in a single line of code. Usually, we would assign
them to a variable.

For example, the following lambda function multiplies a number by 2 and then adds 3:

    mylambda = lambda x: (x * 2) + 3
    print(mylambda(5))

The output:

    > 13

Lambda functions work with all types of variables, not just integers! Here is an example that takes
in a string, assigns it to the temporary variable x, and then converts it into lowercase:

stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!"))

The output:

    > "oh hi mark!"
"""

# Create a lambda function mylambda that returns the first and last letters of a string, assuming
# the string is at least 2 characters long. For example,

print(mylambda("This is a string"))

# should produce:
# 'Tg'

mylambda = lambda x: x[0] + x[-1]

"""

We can make our lambdas more complex by using a modified form of an if statement.

Suppose we want to pay workers time-and-a-half for overtime (any work above 40 hours per week). The
following function will convert the number of hours into time-and-a-half hours using an if
statement:

def myfunction(x):
    if x > 40:
        return 40 + (x - 40) * 1.50
    else:
        return x

Below is a lambda function that does the same thing:

myfunction = lambda x: 40 + (x - 40) * 1.50 if x > 40 else x

In general, the syntax for an if function in a lambda function is:

lambda x: [OUTCOME IF TRUE] if [CONDITIONAL] else [OUTCOME IF FALSE]

"""

# You are managing the webpage of a somewhat violent video game and you want to check that each
# user’s age is 13 or greater when they visit the site.

# Write a lambda function that takes an inputted age and either returns Welcome to BattleCity! if
# the user is 13 or older or You must be over 13 if they are younger than 13. Your lambda function
# should be called mylambda.

mylambda = lambda x: "Welcome to BattleCity!" if x >= 13 else "You must be over 13"

