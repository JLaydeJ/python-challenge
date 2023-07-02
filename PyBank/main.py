import os
import csv

#Set variable for
budget_csv_path = os.path.join("Resources","budget_data.csv")

#Lists to store data
Months = []
Profit_Losses = []
Profit_Losses_Change = []

#Set inital values
#Total_Months = 0 

#Open CSV file
with open(budget_csv_path, newline='') as csvfile:
    #Seperate data by comma ','
    budget_reader = csv.reader(csvfile, delimiter=',')

    #Skip the header row
    next(budget_reader)

    #Create table that excludes first row
    Budget_Table = [next(budget_reader)]

    #Set inital previous profit/losses net amounts
    Previous_Total = int(Budget_Table[0][1])

    #Set initial number of months excluded in table created 
    Initial_Month = 1

    #Set initial number of profit/losses excluded in table created 
    Initial_Profit_Losses = 1088983
    
    #Create Loop to loop through CSV File
    for row in budget_reader:
        #Add months/dates
        Months.append(row[0])

        #The total number of months included in the dataset plus inital month
        Total_Months = len(Months) + Initial_Month
       
        #Add profit/losses
        Profit_Losses.append(int(row[1]))

        #The net total amount of "Profit/Losses" over the entire period
        Total_ProfLoss = sum(Profit_Losses) + Initial_Profit_Losses

        #Tried setting Changes = 0 and got syntac error
        #Tried setting Changes = [] inside loop but got -224669.0, so I put Changes = [] outside loop
        #Add changes ; The changes in "Profit/Losses" over the entire period
        Profit_Losses_Change.append(int(row[1]) - Previous_Total)

        #The average of those changes
        Average = sum(Profit_Losses_Change) / len(Profit_Losses_Change)

        #Re-define/Store new previous profit/losses net amount
        Previous_Total = int(row[1]) 

    #The greatest increase in profits amount over the entire period (use max function)
    Greatest_Increase_Profit = max(Profit_Losses_Change)

    #The greatest decrease in profits amount over the entire period (use max function)
    Greatest_Decrease_Profit = min(Profit_Losses_Change)
    
    #The greatest increase/decrease in profit dates (use index function)
    Increase_Index = Profit_Losses_Change.index(Greatest_Increase_Profit)
    Decrease_Index = Profit_Losses_Change.index(Greatest_Decrease_Profit)
    Greatest_Increase_Dates = Months[Increase_Index]
    Greatest_Decrease_Dates = Months[Decrease_Index]

#Print output to Terminal
Print = f'''Financial Analysis\n-------------------------
Total Months: {Total_Months}\nTotal: {Total_ProfLoss}\nAverage Change: ${Average:.2f}
Greatest Increase in Profits: {Greatest_Increase_Dates} (${Greatest_Increase_Profit}
Greatest Increase in Profits: {Greatest_Decrease_Dates} (${Greatest_Decrease_Profit})'''
print(Print)

# Set variable for output file
budget_csv_path = os.path.join("Analysis","Financial_Analysis.txt")

#  Open the output file
with open(budget_csv_path, "w") as textfile:

    #Write to textfile
    textfile.write(Print)