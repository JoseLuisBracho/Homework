import os
import csv

currentDir =  os.getcwd()
print(currentDir)
file = os.path.join(currentDir, "pyBank", "Resources","budget_data.csv")

# Reads and accomodates the data into list
with open(file, 'r', newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    dates = []
    profLoss = []
    for row in csvreader:
        dates.append(row[0])
        profLoss.append(float(row[1]))

# Number of months and total profit
num_mo = len(dates)
sum_prof_loss = sum(profLoss)
avg_prof_loss = sum_prof_loss / num_mo

# Fill the profit changes vector (list)
change = []
for i in range(1, num_mo):
    change.append(profLoss[i]-profLoss[i-1])

# Calculates max and min in profit changes, also its dates
min_mo_prof = [(i, val) for i, val in enumerate(change) if val == min(change)]
max_mo_prof = [(i, val) for i, val in enumerate(change) if val == max(change)]

# Shows results to the terminal
print('\nFinancial Analysis')
print('--------------------------------')
print(f"Total Months: {num_mo}")
print(f"Total: ${sum_prof_loss:0.0f}")
print(f"Average Change: ${(sum(change) / len(change)):0.2f}")
print(f"Greatest Increase in Profits: {dates[max_mo_prof[0][0] + 1]} (${max_mo_prof[0][1]:0.0f})")
print(f"Greatest Decrease in Profits: {dates[min_mo_prof[0][0] + 1]} (${min_mo_prof[0][1]:0.0f})")


# Write results to a csv file
output_file = os.path.join(currentDir, "pyBank", "Resources", "results_analysis.txt")
with open(output_file, 'w', newline='') as txtfile:
    #txtfile = csv.writer(csvfile, delimiter=" ")
    txtfile.write("Finantial Analysis\n")
    txtfile.write("--------------------------------\n")
    txtfile.write(f"Total Months: {num_mo}\n")
    txtfile.write(f"Total: ${sum_prof_loss:0.0f}\n")
    txtfile.write(f"Average Change: ${(sum(change) / len(change)):0.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {dates[max_mo_prof[0][0] + 1]} (${max_mo_prof[0][1]:0.0f})\n")
    txtfile.write(f"Greatest Decrease in Profits: {dates[min_mo_prof[0][0] + 1]} (${min_mo_prof[0][1]:0.0f})\n")