import csv

def main():
    
    infile = open('customers.csv' , 'r')
    outfile = open('customers_country' , 'w')
    csvfile = csv.reader(infile, delimiter=',')
    writer = csv.writer(outfile)
    next(csvfile)
    outfile.write("Full Name" + ", " + "Country" + "\n")
    count = 1

    for record in csvfile:
        outfile.write(record[1] + " " + record[2] + ', ')
        outfile.write(record[4])
        outfile.write("\n")
        count += 1 

    
    print("Number of Customers read from the file: ", count)

main()