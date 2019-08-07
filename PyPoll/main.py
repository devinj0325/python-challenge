#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

#import
import os
import csv

csvpath = os.path.join("election_data.csv")

#variables - total votes, candidate (list), count # of votes, 
# winner total votes
Vote_total = 0
candidate = []
CountVote = []
winnerCountVote = 0

with open(csvpath, newline='') as csvfile:        
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Loop
    for row in csvreader:
        #Vote counter
        Vote_total += 1
        #list
        #my_list.append(object)
        if(row[2] not in candidate):
            candidate.append(row[2]) #row 2 - not header
            CountVote.append(0) #keep line below in if statement - but dont indent
        candidateIndex = candidate.index(row[2]) #where candidate row starts
        CountVote[candidateIndex] += 1 #count from 1 
    #Print
    #\n whitespace
    print(f"\nElection Results\n--------------------")
    print(f"Total votes: {Vote_total}")
    print("-----------------------")
    
    #count votes
    for x in range(len(candidate)): #use round & len for amount of candidates
        votePercent = round((CountVote[x]/Vote_total) * 100)
        print(f"{candidate[x]}: {votePercent}% ({CountVote[x]})") #f string
        if (winnerCountVote<CountVote[x]):
            winnerCountVote = CountVote[x]
            winner = candidate[x]
            #print(winner)
    
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

file = open('output.txt','w')
# \n whitespace
#.txt output   
file.write("Election Results")
file.write("\n------------------------")
file.write("\nTotal votes:" + str(Vote_total))
file.write("\n------------------------")
# "%" \n creates whitespace
for x in range(len(candidate)):
    votePercent = round((CountVote [x] / Vote_total)*100)
    file.write("\n" + str(candidate [x] ) +" : " + str(votePercent) 
        + "% ("+ str(CountVote [x] ) + ")")
file.write("\n-------------------------")
file.write("\nWinner: " + str(winner))
file.write("\n-------------------------")
file.close()