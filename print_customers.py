import csv

infile = open('customers.csv' , 'r')

csvfile = csv.reader(infile, delimiter=',')


next = input("Press Enter to View another record.")
for record in csvfile:
    print('student ID:', record[0])
    print('fname:', record[1])
    print('lname:' , record[2])
    print('City:' , record[3])
    print('Country:' , record[4])
    print('Phone:' , record[5])

    input()
    
