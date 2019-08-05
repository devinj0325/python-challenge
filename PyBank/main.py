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
    print(f"Average Change : ${round(total_revenue/len(dates),2)}")
    print(f"Greatest Increase in Profits : {maxProfitMonth} ({maxProfit})")
    print(f"Greatest Decrease in Profits : {minProfitMonth} ({minProfit})")