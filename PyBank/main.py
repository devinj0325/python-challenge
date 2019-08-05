import os
import csv

csvpath = os.path.join("Desktop", "Github", "python-challenge","PyBank","budget_data.csv")

with open(csvpath, 'r', newline='') as csvfile:    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #variables
    dates = []
    total_rev = 0
    maxProfit = 0
    minProfit = 0
    
    #Looping through data in csv file
    for row in csvreader:
        dates.append(row[0])
        #Add revenue
        total_rev += int(row[1])

        #Maximum profit
        if(maxProfit<int(row[1])):
            maxProfit = int(row[1])
            maxProfitMonth = row[0]
        
        #Min profit
        if(minProfit>int(row[1])):
            minProfit = int(row[1])
            minProfitMonth = row[0]
    
    #Print
    print("\nFinancial Analysis\n-----------------------------------------------")
    print(f"Total Month: {len(dates)}")
    print(f"Total Revenue : ${total_rev}")
    print(f"Average Change : ${round(total_rev/len(dates),2)}")
    print(f"Greatest Increase in Profits : {maxProfitMonth} ({maxProfit})")
    print(f"Greatest Decrease in Profits : {minProfitMonth} ({minProfit})")