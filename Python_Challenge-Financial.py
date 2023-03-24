import os
import csv

#value placeholders
budget_date = []
budget_pl = []
total_months = -1
total_total= 0
#starting Values
grt_in= 0
grt_dc= 1000000000

#csv pathing
budget_path = os.path.join('Resources', 'budget_data.csv')
with open(budget_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #building lists
        budget_date.append(row[0])
        budget_pl.append(row[1])

#counting dates
for x in budget_date:
    total_months = total_months + 1

#profit/ loss calculations
for i  in budget_pl[1:]:
    total_total = total_total + int(i)
    if int(i) > grt_in:
        grt_in = int(i)
    elif int(i) < grt_dc:
        grt_dc = int(i)
avg_change = total_total / total_months

#txt output
with open('Analysis/Financial_Analysis.txt', 'w') as f:
    f.write(f"Financial Analysis\n")
    f.write(f"---------------------------\n")
    f.write(f"Total Months:  {str(total_months)}\n")
    f.write(f"Total: {str(total_total)}\n") 
    f.write(f"Average Change: {str(avg_change)}\n")
    f.write(f"Greatest Increase in Profits: {str(grt_in)}\n")
    f.write(f"Greatest Decrease in Profits: {str(grt_dc)}\n")