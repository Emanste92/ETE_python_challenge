import os
import csv
bank_csv = os.path.join("./budget_data.csv")

months = 0
netTotal = 0 
averageChange = 0


print(bank_csv)
with open(bank_csv,newline="") as bankcsvfile:
    csvreader = csv.reader(bankcsvfile,delimiter=",")
    # print(csvreader)
    # prints header to remove it from subsequent for loop
    csv_header = next(csvreader)
    # print(csv_header)
    # for loop
    for row in csvreader:
        months = months + 1
        netTotal += int(row[1])
        
    
# Printing Output
print()
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {months}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${averageChange}")
# print(f"Greatest Increase in Profits: {  } (${  })")
# print(f"Greatest Decrease in Profits: {  } (${  })")
# output = open("bank_data.txt","w")
