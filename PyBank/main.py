#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

# import 
import os
import csv
# path to data file
csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline='') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #variables
    dates = []
    total_revenue = 0
    maxProfit = 0
    minProfit = 0
    
    #Looping through data in csv file
    for row in csvreader:
        dates.append(row[0])
        #revenue
        total_revenue += int(row[1])

        #Maximum profit
        if(maxProfit<int(row[1])):
            maxProfit = int(row[1])
            maxProfitMonth = row[0]
        
        #Min profit
        if(minProfit>int(row[1])):
            minProfit = int(row[1])
            minProfitMonth = row[0]
    
    #Print
    print("\nFinancial Analysis\n-----------------------")
    print(f"Total Months: {len(dates)}")
    print(f"Total: ${total_revenue}")
    #for average use round
    print(f"Average Change : ${round(total_revenue/len(dates))}")
    print(f"Greatest Increase in Profits : {maxProfitMonth} ({maxProfit})")
    print(f"Greatest Decrease in Profits : {minProfitMonth} ({minProfit})")

    #export text file - https://www.w3schools.com/python/python_file_open.asp & https://www.geeksforgeeks.org/reading-writing-text-files-python/
    file = open('pybank_financial.txt','w')
    file.write("Financial Analysis\n----------------------")
    file.write("\nTotal Months: " + str(len(dates)))
    file.write("\nTotal Revenue : $" + str(total_revenue))
    file.write("\nAverage Change : $" + str(round(total_revenue/len(dates))))
    file.write("\nGreatest Increase in Profits : " + str(maxProfitMonth) + " (" + str(maxProfit) + ")")
    file.write("\nGreatest Decrease in Profits : " + str(minProfitMonth) + " (" + str(minProfit) + ")")
    file.close()

