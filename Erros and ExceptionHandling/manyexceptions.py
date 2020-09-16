# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
    result = 10 + '10'
except NameError:
    print("Hey it looks like you arent adding correctly!")
else:
    print(result)

