x =10
#if there is an error it prints something else
try:
  print(x)
except:
  print("An exception occurred")

try:
    result = 10 + 10
except:
    print("Hey it looks like you arent adding correctly!")
else:
    print(result)