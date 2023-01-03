import sys
import csv

ret = []

csvfile = open(sys.argv[1],"r",newline="")
reader = csv.reader(csvfile)
for row in reader:
    ret.append(row)

print(ret)
