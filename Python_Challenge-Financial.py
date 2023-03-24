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
#print(total_months)

#profit/ loss calculations
for i  in budget_pl[1:]:
    total_total = total_total + int(i)
    if int(i) > grt_in:
        grt_in = int(i)
    elif int(i) < grt_dc:
        grt_dc = int(i)
avg_change = total_total / total_months

#print check
#print(total_total)
#print(total_months)
#print(avg_change)
#print(grt_in)
#print(grt_dc)

#txt output
with open('Analysis/Financial_Analysis.txt', 'w') as f:
    f.write(f"Financial Analysis\n")
    f.write(f"---------------------------\n")
    f.write(f"Total Months:  {str(total_months)}\n")
    f.write(f"Total: {str(total_total)}\n") 
    f.write(f"Average Change: {str(avg_change)}\n")
    f.write(f"Greatest Increase in Profits: {str(grt_in)}\n")
    f.write(f"Greatest Decrease in Profits: {str(grt_dc)}\n")


#output_file = "Analysis/Financial_Analysis.txt"
#with open(output_file, 'w') as file_writter:
    #writter = 


#budget_data setup:
#column 1 = Date
#column 2 = Profit/ loss
#row 1 = Titles
#Rows 2 to 87 = Data

#budget_data Goal:
#Header: "Financial Analysis"
#Seperator: "---------------------------"
#"Total Months: " + (# of unique rows in column 1)
#"Total: " + (sum of column 2)
#"Average Change: " + "$" + (average of column 2)
#"Greatest Increase in Profits: " + ?? Date X ($X) ?? {#1 Header?}
#"Greatest Decrease in Profits: " + ?? Date X ($X) ?? {#1 Tail?}
#export results into Analysis as file "Financial_Analysis.txt"