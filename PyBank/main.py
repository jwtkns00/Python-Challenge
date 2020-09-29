#import dependencies
import os
import csv

#set path for csv file
file_to_load = os.path.join("Desktop", "budget_data.csv")

#read and open csv file
with open(file_to_load, newline="") as f:
    csvreader = csv.reader(f, delimiter=",")
    csv_header = next(f)
    
    #make new dictionaries
    PL = []
    months = []
    change = []

    # start for loop
    for rows in csvreader:
        PL.append(int(rows[1]))
        months.append(rows[0])
   
    for i in range(1, len(PL)):
        change.append((int(PL[i]) - int(PL[i-1])))
    
    #find values
    totalmonths = len(months)
    average = sum(change) / len(change)
    greatest_decrease = min(change)
    greatest_increase = max(change)

    # Print summary table
    print("Financial Analysis")
    print("....................................................................................")
    print("Total Months: " + str(totalmonths))
    print("Total: " + "$" + str(sum(PL)))
    print("Average change: " + "$" + str(average))
    print("Greatest Increase in Profits: " + str(months[change.index(max(change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[change.index(min(change))+1]) + " " + "$" + str(greatest_decrease))

    #output .txt file
    data = open("budget_data.txt","w")
    data.write("Financial Analysis" + "\n")
    data.write("...................................................................................." + "\n")
    data.write("Total Months: " + str(totalmonths) + "\n")
    data.write("Total: " + "$" + str(sum(PL)) + "\n")
    data.write("Average Change: " + "$" + str(average) + "\n")
    data.write("Greatest Increase in Profits: " + str(months[change.index(max(change))+1]) + " " + "$" + str(greatest_increase) + "\n")
    data.write("Greatest Decrease in Profits: " + str(months[change.index(min(change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
    data.close()



