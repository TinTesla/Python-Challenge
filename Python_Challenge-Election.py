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
        #building list
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

#percent calculations
p_charles = round(votes_charles / total_votes *100, 2)
p_charles = str(p_charles) + "%"
p_diana = round(votes_diana / total_votes *100, 2)
p_diana = str(p_diana) + "%"
p_raymon = round(votes_raymon / total_votes *100, 2)
p_raymon = str(p_raymon) + "%"

#winner check
if votes_charles > votes_diana and votes_charles > votes_raymon:
    votes_winner = "Charles Casper Stockham"
elif votes_diana > votes_charles and votes_diana > votes_raymon:
    votes_winner = "Diana DeGette"
elif votes_raymon > votes_charles and votes_raymon > votes_diana :
    votes_winner = "Raymon Anthony Doane"

#txt output
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