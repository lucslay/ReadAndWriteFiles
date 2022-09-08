
#Import the csv library b/c we need it
import csv

def main():
    
    #open the file we will use and the one we will print two, along with the reader and the writer
    infile = open('steps.csv','r')
    reader = csv.reader(infile, delimiter=',')
    outfile = open('avg_steps.csv','w')
    csv_writer = csv.writer(outfile, delimiter=',')

    #Skip infile header
    next(reader)

    numDays = 0
    monthlyTotal = 0
    month = 0

    #Make this to be able to reference numbers to months
    monthsList = ['January', 'February', 'March', 'April',
    'May', 'June', 'July', 'August', 'September','October', 
    'November', 'December']

    #header
    csv_writer.writerow(["Month of the year", "Average Steps walked in the Month"])

    for row in reader:

        if month == 0 or int(row[0]) == month:
        
            monthlyTotal += int(row[1])
            numDays += 1
            month = int(row[0])

        else:

            monthlyTotal /= numDays
            numDays = 1
            totalMonths = monthsList[month-1]
            twoDecimals = "{:.2f}".format(monthlyTotal)
            outfile.write(totalMonths + ',' + str(twoDecimals) +'\n')
            month = 0
            monthlyTotal = int(row[1])

    #December
    monthlyTotal /= numDays
    numDays = 0
    
    totalMonths = monthsList[month-1]
    twoDecimals = "{:.2f}".format(monthlyTotal)
    
    outfile.write(totalMonths + ',' + str(twoDecimals))

    #Close the two files
    outfile.close()
    infile.close()

main()