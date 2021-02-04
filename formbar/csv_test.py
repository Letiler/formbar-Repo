import csv

with open('testing.txt', mode='r') as csv_file:
    data = csv.reader(csv_file)
    data = list(data)
    print(data)
