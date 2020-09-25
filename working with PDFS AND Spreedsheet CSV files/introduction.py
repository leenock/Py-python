# CSV stands fro comma separated variables and is a very common output for spreedsheet programs

# example
# Name , Hours , Rate
# David, 20, 15
# Claire, 40, 20

import csv

# open the file
data = open('example.csv',encoding='utf-8')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a python object list of lists
data_lines = list(csv_data)
print(data_lines)
print('\n')
# check the fist row which contains the titles
print(data_lines[0])
print('\n')
# check the number of rows including the title rows
print(len(data_lines))

print('\n')
# print rows upto row five

for lines in data_lines[:5]:
    print(lines)
print('\n')
# print row 10
print(data_lines[10])

print('\n')
# extract a single value

print(data_lines[10][3])

print('\n')
# entire column for email address

all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
print(all_emails)

print('\n')
# print a list of full names

full_name = []

for line in data_lines[1:3]:
    full_name.append(line[1]+' '+line[2])
print(full_name)

print('\n')
# how to write to a csv file
file_to_output = open('to_save_file.csv',mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()


# append but not over write it

f = open('to_save_file.csv',mode='a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['1','2','8'])
f.close()