import csv

data = open('find_the_link.csv',encoding='utf-8')
csv_data = csv.reader(data)
print(csv_data)

data_lines = list(csv_data)
print(data_lines[0])

link_str = ''

for row_num,data in enumerate(data_lines):
    link_str += data[row_num]

print(link_str)

# Grap the Google link Drive link from the .csv file