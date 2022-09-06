import csv

infile = open ("EmployeePay.csv" , "r")
csvreader = csv.reader(infile, delimiter=",")
for row in infile:
    print(row)