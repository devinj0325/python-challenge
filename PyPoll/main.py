#import
import os
import csv

csvpath = os.path.join("election_data.csv")

#variables
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
            candidate.append(row[2])
            CountVote.append(0) #keep line below in if statement - but dont indent
        candidateIndex = candidate.index(row[2]) #where candidate row starts
        CountVote[candidateIndex] += 1 #count from 1 
    #Print
    print(f"\nElection Results\n--------------------")
    print(f"Total votes: {Vote_total}")
    print("-----------------------")
    
    for x in range(len(candidate)): #use round & len for amount of candidates
        votePercent = round((CountVote[x]/Vote_total) * 100)
        print(f"{candidate[x]}: {votePercent}% ({CountVote[x]})")
        if (winnerCountVote<CountVote[x]):
            winnerCountVote = CountVote[x]
            winner = candidate[x]
            #print(winner)
    
    print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

file = open('output.txt','w')

#.txt output   
file.write("Election Results")
file.write("\n------------------------")
file.write("\nTotal votes:" + str(Vote_total))
file.write("\n------------------------")
    
for x in range(len(candidate)):
    votePercent = round((CountVote [x] /Vote_total)*100)
    file.write("\n" + str(candidate [x] ) +" : " + str(votePercent) 
        + "% ("+ str(CountVote [x] ) + ")")
file.write("\n-------------------------")
file.write("\nWinner: " + str(winner))
file.write("\n-------------------------")
file.close()