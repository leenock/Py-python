import os
os.remove("myfile.txt")

# check if the file exist

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
