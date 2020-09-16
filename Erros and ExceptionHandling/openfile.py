f = open("demofile.txt", "r")
print(f.read())

# open file in a diffrent location

# Open the file "demofile2.txt" and append content to the file:
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())



# Open the file "demofile3.txt" and overwrite the content:
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content again again!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

# create a new file

#f = open("myfile.txt", "x")
f = open("myfile.txt", "w")
f.write("i have created a new file using the x mode")

f = open("myfile.txt", "r")
print(f.read())