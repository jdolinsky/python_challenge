import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')

# Report header
header ="""

      Election Results
      
--------------------------------------------------------
      """
total_votes = 0
#create a dictionary where we will store votes per candidate
votes_counter = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1
        #check if the key with canditate name exists in the counter
        #if it does, increment 
        if row[2] in votes_counter:
            votes_counter[row[2]] += 1
        else: 
            #otherwise create a new dictionary porperty with new key and value 1
            votes_counter[row[2]] = 1

print(f"total votes {votes_counter}")

print(f"Total Votes: {total_votes: ,} \n")