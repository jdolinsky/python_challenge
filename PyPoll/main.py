import csv
import os

csvpath = os.path.join('Resources', 'election_data.csv')
#separator
separator = "------------------------------------------------"
# Report header
header = "Election Results"
total_votes = 0
#create a dictionary where we will store votes per candidate
votes_counter = {}
#a string to output total votes per candidate
vote_totals = ""

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

# find a key with max votes
max_key = max(votes_counter, key=lambda k: votes_counter[k])

for key, value in votes_counter.items():
    vote_totals += f"{key}: {value/total_votes:.3%} ({value:,}) \n\n"

#buld summary
summary = f"""
{header}\n
{separator}\n
Total Votes: {total_votes: ,}\n
{separator} \n
{vote_totals}{separator}\n
Winner: {max_key}\n
{separator}
"""
print(summary)

# write results in a .txt file
f = open("./analysis/myfile.txt", "w")
f.write(summary)
f.close()