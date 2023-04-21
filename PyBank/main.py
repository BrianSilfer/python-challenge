import os
import csv


#print(os.getcwd())

file = '/Users/briansilfer/Desktop/git/python-challenge/PyBank/Resources/budget_data.csv'
  
#create sum function for total pl
def sum(num_list):
    y =0
    for num in num_list:
        y = (y + int(num))
    return y
#create avg function for pl changes
def avg(num_list):
    y =0
    for num in num_list:
        y = (y + int(num))
    return y/len(num_list)
#create change function for pl
def change(num_list):
    # change variable consists of finding the previous num value - current num value then negating it to get the
    #difference between the current value and previous value
    
    return change

with open(file,'r') as csv_file:
    #read csv file
    csvreader = csv.reader(csv_file, delimiter=",")
    #set row count variable to 0 for Month Total
    row_count = 0
    #create variable for p/l
    pl_total = 0
    # create variable for header
    header = next(csvreader)
    #create header indexes for later use
    date_index = header.index("Date")
    pl_index = header.index("Profit/Losses")
    #Create lists to store data and change
    date = []
    profit_loss = []
    change = []
    #create dictionary of dates and pl values
    pybank_dict = {"dates":[],"profit/loss":[],"change":[]}
    #loop through csv to find variables for output
    for row in csvreader: 
        #row count to find number of rows in file/Total number of months
        row_count += 1
        

        #add profit loss to pl list and pybank dict
        profit_loss.append(row[1])
        pybank_dict["profit/loss"].append(row[1])

        # code to turn each list entry from a str into an int
        for i in range(0,len(profit_loss)):
            profit_loss[i] = int(profit_loss[i])
        
        #add dates to date list and pybank dictionary
        if row[0] not in date:
            date.append(row[0])
            pybank_dict["dates"].append(row[0])
        #create change list taking the profit and subtracting the previous value over length 1 to length of list
        change_list = [profit_loss[x] -profit_loss[x-1] for x in range(1, len(profit_loss))]
        #add change to change list
        change.append(change_list)
        #add change list to py_bank dict
        pybank_dict["change"]=change_list


#Print Financial Analysis
print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {row_count}")
print(f'Total: ${sum(profit_loss)}')
print(" ")
print(f'Average Change: ${round(avg(change_list),2)}')
print(" ")
#Greatest increase calculation Plus 1 because the index of change_list starts at 1 due to the nature of change
#needing a previous value, Adding 1 puts the change list on the same index as the dates values
print(f'Greatest Increase in Profits:{pybank_dict["dates"][change_list.index(max(change_list))+1]} (${max(change_list)})')
print(" ")
#Greatest Decrease Calculation, Plus 1 because the index of change_list starts at 1 due to the nature of change
#needing a previous value, Adding 1 puts the change list on the same index as the dates values
print(f'Greatest Decrease in Profits:{pybank_dict["dates"][change_list.index(min(change_list))+1]} (${min(change_list)})')


# save the output file path
output_file= '/Users/briansilfer/Desktop/git/python-challenge/PyBank/analysis/pybank_analysis.txt'
#writing output lines to be joined by \n
output_lines = (f'Financial Analysis\n'
                '---------------------------------------','\n'
                'Total Months: 86''\n',
                'Total: $22564198''\n',
                'Average Change: $-8311.11''\n',
                'Greatest Increase in Profits: Aug-16 ($1862002)''\n',
                'Greatest Decrease in Profits: Feb-14 ($-1825558)')

#Writing text file to output path
with open(output_file,'w') as file:
    file.write('\n'.join(output_lines))
    

