# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.

x = -1
z = "hello"

if x < 0:
  raise Exception('Sorry, no numbers below zero')



if not type(z) is int:
  raise TypeError("Only integers are allowed")