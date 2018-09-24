import os
import csv

poll_csv = os.path.join("./election_data.csv")

voters = 0

winner = 0

print(poll_csv)
with open(poll_csv,newline="") as pollcsvfile:
    csvreader = csv.reader(pollcsvfile,delimiter=",")
    # print(csvreader)
    # prints header to remove it from subsequent for loop
    csv_header = next(csvreader)
    # print(csv_header)
    # for loop
    for row in csvreader:
        voters = voters + 1
        
        
    
# Printing Output
print()
print("Election Results")
print("-------------------------")
print(f"Total Votes: {voters}")
print("-------------------------")
# print(f"  {   }")
# print(f"  {   }")
# print(f"  {   }")
# print(f"  {   }")
print("-------------------------")
# print(f"Winner: {  }")
# output = open("poll_data.txt","w")

