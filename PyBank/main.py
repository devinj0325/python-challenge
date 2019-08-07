#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period

# import 
import os
import csv
import statistics # do the math for me

csvpath = os.path.join("budget_data.csv")
#variables
Dates = 0
totalProfit = 0
maxProfit = 0
maxProfitMonth = ''
minProfit = 0
minProfitMonth = ''

change = []
monthToMonthChange = [] #for avg change

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
 #Looping through data in csv file
    for row in csvreader:
        #print(row)
        Dates += 1
        #revenue
        totalProfit += int(row[1])
        #max
        if int(row[1]) > maxProfit:
            maxProfitMonth = (row[0])
            maxProfit = int(row[1])
        #min
        elif int(row[1]) < minProfit:
            minProfitMonth = (row[0])
            minProfit = int(row[1])
        change.append(int(row[1]))

  
# MONTHLY CHANGE
for i in range(len(change)-1):
    monthlyChange = (change[i+1] - change[i])
    monthToMonthChange.append(monthlyChange)   
#import statistics
averageChange = statistics.mean(monthToMonthChange)
# print
print("Financial Analysis")
print("--------------------------------")

print("Total Months: " + str(Dates))
print("Total: $" + str(totalProfit))
print("Average Change is: $" + str(round(averageChange, 2))) # ,2 numbers after decimal
print("Greatest Increase in Profits: " + str(maxProfitMonth) + "  ($" + str(maxProfit) + ")")
print("Greatest Decrease in Profits: " + str(minProfitMonth) + "  ($" + str(minProfit) + ")")

# output file
 #export text file - https://www.w3schools.com/python/python_file_open.asp & https://www.geeksforgeeks.org/reading-writing-text-files-python/
file = open('pybank_financial.txt','w')
file.write("Financial Analysis")
file.write("----------------------------")

file.write("Total Months: " + str(Dates))
file.write("Total: $" + str(totalProfit))
file.write("Average Change is: $" + str(round(averageChange, 2))) # ,2 numbers after decimal
file.write("Greatest Increase in Profits: " + str(maxProfitMonth) + "  ($" + str(maxProfit) + ")")
file.write("Greatest Decrease in Profits: " + str(minProfitMonth) + "  ($" + str(minProfit) + ")")
