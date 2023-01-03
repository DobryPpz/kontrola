import csv
import sys

with open(sys.argv[1], mode='r') as csv_file:
    #csv_reader = csv.DictReader(csv_file)
    csv_reader = csv.reader(csv_file)
    line_count = 0
    listL = []
    for row in csv_reader:
        listL.append(row)
    print(listL)
        

