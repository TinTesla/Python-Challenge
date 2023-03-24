import os
import csv

#value placeholders
el_canidate = []
total_votes= -1
votes_charles= 0
votes_diana= 0
votes_raymon= 0
votes_winner=0

#csv pathing
budget_path = os.path.join('Resources', 'election_data.csv')
with open(budget_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #building lists
        el_canidate.append(row[2])

#counting votes
for x in el_canidate:
    total_votes = total_votes + 1
    if x == "Charles Casper Stockham":
        votes_charles = votes_charles + 1
    elif x == "Diana DeGette":
        votes_diana = votes_diana + 1
    elif x == "Raymon Anthony Doane":
        votes_raymon = votes_raymon + 1

#print check
    #print(total_votes)
    #print(votes_charles)
    #print(votes_diana)
    #print(votes_raymon)

#percent calculations
p_charles = round(votes_charles / total_votes *100, 2)
p_charles = str(p_charles) + "%"
p_diana = round(votes_diana / total_votes *100, 2)
p_diana = str(p_diana) + "%"
p_raymon = round(votes_raymon / total_votes *100, 2)
p_raymon = str(p_raymon) + "%"

#print check
    #print(p_charles)
    #print(p_diana)
    #print(p_raymon)

#winner check
if votes_charles > votes_diana and votes_charles > votes_raymon:
    votes_winner = "Charles Casper Stockham"
elif votes_diana > votes_charles and votes_diana > votes_raymon:
    votes_winner = "Diana DeGette"
elif votes_raymon > votes_charles and votes_raymon > votes_diana :
    votes_winner = "Raymon Anthony Doane"
#print(votes_winner)


with open('Analysis/Election_Analysis.txt', 'w') as f:
    f.write(f"Election Results\n")
    f.write(f"---------------------------\n")
    f.write(f"Total Votes:  {str(total_votes)}\n")
    f.write(f"---------------------------\n")
    f.write(f"Charles Casper Stockham: {str(p_charles)}\n")
    f.write(f"Diana DeGette: {str(p_diana)}\n")      
    f.write(f"Raymon Anthony Doane: {str(p_raymon)}\n") 
    f.write(f"---------------------------\n")           
    f.write(f"Winner: {str(votes_winner)}\n")


#election_data setup:
#column 1 = Ballot ID
#column 2 = Country
#column 3 = Canidate
#row 1 = Titles
#rows 2 to 369712 = Data

#election_data Goal:
#Header: "Election Results"
#Seperator: "---------------------------"
#Total Votes: >>(sum of unique rows in column 1)
#Seperator: "---------------------------"
#"Charles Casper Stockham: " + [(Countif column 3 = Charles Casper Stockham)/ sum of column 3] + "%" + "(" + Countif column 3 = Charles Casper Stockham + ")"
#"Diana DeGette: " + [(Countif column 3 = iana DeGette)/ sum of column 3] + "%" + "(" + Countif column 3 = Diana DeGette + ")"
#"Raymon Anthony Doane: " + [(Countif column 3 = Raymon Anthony Doane)/ sum of column 3] + "%" + "(" + Countif column 3 = Raymon Anthony Doane + ")"
#Seperator: "---------------------------"
#"Winner: " + ?? Entry with most results in column 3
#export results into Analysis as file "Election_Analysis.txt"