# importing packages and data csv
import os
import csv
poll_csv = os.path.join("./election_data.csv")

# defining lists and variables
voters = 0
voterID = []
candidate = []
voteDict = {}
winner = 0


# opening and defining csvreader to manipulate further
with open(poll_csv,newline="") as pollcsvfile:
    csvreader = csv.reader(pollcsvfile,delimiter=",")
    # prints header to remove it from subsequent for loop
    csv_header = next(csvreader)
    # print(csv_header)
    # for loop
    for row in csvreader:
        voters = voters + 1
        voterID.append(row[0])
        candidate.append(row[2])
        voteDict = dict(zip(voterID, candidate))
    #print(voteDict)
        
    
    #winner = max()

# printing data summary
print()
print("Election Results")
print("-------------------------")
print(f"Total Votes: {voters}")
print("-------------------------")
# print(f"{   }: {round(   , 2)}% ({  }) ")
# print(f"{   }: {round(   , 2)}% ({  }) ")
# print(f"{   }: {round(   , 2)}% ({  }) ")
# print(f"{   }: {round(   , 2)}% ({  }) ")
print("-------------------------")
# print(f"Winner: {winner}")


# putting data summary as a .txt file output
# output = open("poll_data.txt","w")

