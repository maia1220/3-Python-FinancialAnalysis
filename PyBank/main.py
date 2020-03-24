# ## PyBank


import os
import csv

# Absolute Path
# csvpath = "/Users/aq/Documents/Classwork/vu-nsh-data-pt-02-2020-u-c/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv"
# Relative Path
csvpath = os.path.join(os.path.expanduser('~'),"Documents/Classwork/vu-nsh-data-pt-02-2020-u-c", "03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv")

def analyze_budget(path):

    # build new variables to store either lists or numbers
    new_budget_dict = []
    month_list = []
    avgchanges = []
    amount_list = []
    total_amount = 0
    changes = 0
    total_changes = 0

    #open the csv file
    with open(csvpath) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            month = row["Date"]
            month_list.append(row["Date"])
            amount = row["Profit/Losses"]
            total_amount += int(row["Profit/Losses"])
            amount_list.append(int(row['Profit/Losses']))
            new_budget_dict.append(
                {
                    "Month": row["Date"],
                    "Amount": row["Profit/Losses"]
                }
            )
        #find the monthly changes
        for x in range(len(amount_list)):
            changes = amount_list[x] - changes
            avgchanges.append(changes)
            total_changes += changes
            changes = amount_list[x] #reset the changes variable to the previous amount

    #create a new list to store the date and monthly changes    
    changes_date_list = list(zip(month_list, avgchanges))
    #find total number of months
    total_months = len(new_budget_dict)
    #find the average change over time in profit
    avgchanges2 = round((total_changes-avgchanges[0])/(total_months-1), 2)
    #find the max increase in profit
    maxprofit= max(changes_date_list, key=lambda x:x[1])
    #find the max decrease in profit
    minprofit=min(changes_date_list, key=lambda x:x[1])

    # Absolute Path
    # outputpath = "/Users/aq/Documents/Classwork/vu-nsh-data-pt-02-2020-u-c/03-Python/Homework/Instructions/PyBank/Resources/pybank.txt"
    # Relative Path
    outputpath = os.path.join(os.path.expanduser('~'),"Documents/Homework/Python-Challenge", "Pybank","output.txt")

    #export the summary table to a text file
    with open(outputpath, "a") as f:
        # Summary Table
        print("Financial Analysis \n----------------------------", file =f)
        print(f'Total Months: {total_months}', file =f)
        print(f'Total: ${total_amount}', file =f)
        print(f'Average Change: ${avgchanges2}', file =f)
        print(f'Greatest Increase in Profits: {maxprofit[0]} (${maxprofit[1]})', file =f)
        print(f'Greatest Decrease in Profits: {minprofit[0]} (${minprofit[1]})', file =f)
        print("----------------------------", file =f)

#Run the function!
analyze_budget(csvpath)
