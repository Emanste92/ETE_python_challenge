# importing packages and data csv
import os
import csv
import sys
bank_csv = os.path.join("./budget_data.csv")

# defining lists and variables
months = []
earnings = []
difList = []
bank_dict = {}
netTotal = 0 
averageChange = 0
greatestProfit = 0
greatestLoss = 0

# opening and defining csvreader to manipulate further
with open(bank_csv,newline="") as bankcsvfile:
    csvreader = csv.reader(bankcsvfile,delimiter=",")
    # printing header to remove it from subsequent for loop
    csv_header = next(csvreader)

# using for loops to create lists and determine the total 
# earned and average change
    for row in csvreader:
        netTotal += int(row[1])
        months.append(row[0])
        earnings.append(row[1])
    for i in range(1, int(len(months))):
        difList.append(int(earnings[i]) - int(earnings[i-1]))
        averageChange = sum(difList) / int(len(months) - 1)
# using max() and min() to find the greatest increase in 
# profits and greatest decrease in losses, as well as 
# their respective months; + 1 to ensure that the first month 
# is not counted so the lists align properly
    greatestProfit = max(difList)
    greatestProfitmonth = months[difList.index(max(difList)) + 1]
    greatestLoss = min(difList)
    greatestLossmonth = months[difList.index(min(difList)) + 1]

# printing data summary
    def dataSummary():
        print()
        print("Financial Analysis")
        print("-------------------------")
        print(f"Total Months: {int(len(months))}")
        print(f"Total: ${netTotal}")
        print(f"Average Change: ${round(averageChange, 2)}")
        print(f"Greatest Increase in Profits: {greatestProfitmonth} (${greatestProfit})")
        print(f"Greatest Decrease in Profits: {greatestLossmonth} (${greatestLoss})")
        return

    dataSummary()

# putting data summary as a .txt file output
#sys.stdout = open('bank_data.txt','w'


# # # trying to figure out how to print print statements
# f = open("bank_data.txt","x")
# f.write()
# f.close()