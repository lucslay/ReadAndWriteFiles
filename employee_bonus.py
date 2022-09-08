import csv

infile = open ("EmployeePay.csv" , "r")
csv_reader = csv.DictReader(infile, delimiter = ',')

idCount = 1
for row in csv_reader:
    newBonus = float(row["Bonus"]) + 1.0
    salaryWithBonus = float(row["Salary"]) * newBonus
    print('Employee ID:', idCount,', Name:', row["EmpFName"] , row["EmpLName"], ', Employee Salary with the Bonus:', salaryWithBonus)
    idCount += 1
    ask = input("Would you like to view the next employee? Press y to continue. Press n to stop.")
    if ask == "n":
        break
