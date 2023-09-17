import csv
import os

csvpath = os.path.join('Resources', 'budget_data.csv')

# Report header
header ="""
--------------------------------------------------------

      Financial Analysis
      
--------------------------------------------------------
      """
# Define a counter for months
count_months = 0
# Define a variable for profit/loss
total_profit_loss = 0
#months array
months = []
#profit array
profit_loss = []
#array to store monthly change
change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:
        count_months +=1
        #populate months list 
        months.append(row[0])
        #convert profit/loss to int
        profit_loss_int = int(row[1])
        #populate profit_loss
        profit_loss.append(profit_loss_int)
        # add profit/loss 
        total_profit_loss += profit_loss_int
#populate array with monthly change
for i in range(len(profit_loss)-1):
    change.append(profit_loss[i+1] - profit_loss[i])

#calculate max increase in profits
max_change_i = 0
min_change_i = 0
max_change = change[0]
min_change = change[0]


for i in range(len(change)-1):
    if(max_change < change[i+1]):
        max_change = change[i+1]
        max_change_i = i
    
    if(min_change > change[i+1]):
        min_change = change[i+1]
        min_change_i = i

average_change = round(sum(change)/len(change), 2)

summary = f"""{header}
Total Months: {count_months} \n
Total: ${total_profit_loss:,} \n
Average Change: ${average_change:,} \n
Greatest Increase in Profits: {months[max_change_i+2]} (${max_change:,}) \n
Greatest Decrease in Profits: {months[min_change_i+2]} (${min_change:,}) \n
"""
print(summary)

# write results in a .txt file
f = open("./analysis/myfile.txt", "w")
f.write(summary)
f.close()


