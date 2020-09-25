# Regression
# The term regression is used when you try to find the relationship between variables.
#
# In Machine Learning, and in statistical modeling, that relationship is used to predict the outcome of future events.

# Linear Regression
# Linear regression uses the relationship between the data-points to draw a straight line through all them.
#
# This line can be used to predict future values.

# In Machine Learning, predicting the future is very important.

# How Does it Work?
# Python has methods for finding a relationship between data-points and to draw a line of linear regression. We will show you how to use these methods instead of going through the mathematic formula.
#
# In the example below, the x-axis represents age, and the y-axis represents speed. We have registered the age and speed of 13 cars as they were passing a tollbooth. Let us see if the data we collected could be used in a linear regression:

# Start by drawing a scatter plot:

import matplotlib.pyplot as plt
from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# Predict Future Values
# Now we can use the information we have gathered to predict future values.
#
# Example: Let us try to predict the speed of a 10 years old car.
#
# To do so, we need the same myfunc() function from the example above:

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)