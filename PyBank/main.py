#importing dependencies
import os
import csv

#setting file path
bank_csv = os.path.join("Resources", "budget_data.csv")

#defining variables
month = 0
months = []
net_profit = 0
profit_list = []
profit_change = []
maxincrease = 0
maxmonth = ' '
maxdecrease = 0
maxdecrease_month = ' '
average_change = 0
#looping through the rows and storing values and lists
with open(bank_csv, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)
   

    for row in csv_reader:
        month += 1
        months.append(row[0])
        net_profit += int(row[1])
        profit_list.append(int(row[1]))

    for x in range(len(profit_list)-1):
        profit_change.append(profit_list[x+1]-profit_list[x])
        maxincrease = max(profit_change)
        maxmonth = profit_change.index(max(profit_change))+1
        maxdecrease = min(profit_change)
        maxdecrease_month = profit_change.index(min(profit_change))+1
        average_change = sum(profit_change) / len(profit_change)

#printing results         
print("Financial Analysis")
print("--------------------------------")
print(f'Total months: {month}')
print(f'Total: ${net_profit}')
print(f'Average Change: ${round(average_change, 2)}')
print(f'Greatest Increase in Profits: {months[maxmonth]} (${maxincrease})')
print(f'Greatest Decrease in Profits: {months[maxdecrease_month]} (${maxdecrease})')

#writing results to .txt file in the correct path
output_path = os.path.join("analysis", "Financial Analysis.txt")
with open(output_path, "w") as file:
 file.write("Financial Analysis" "\n")
 file.write("--------------------------------" "\n")
 file.write(f'Total months: {month}')
 file.write("\n")
 file.write(f'Total: ${net_profit}')
 file.write("\n")
 file.write(f'Average Change: ${round(average_change, 2)}')
 file.write("\n")
 file.write(f'Greatest Increase in Profits: {months[maxmonth]} (${maxincrease})')
 file.write("\n")
 file.write(f'Greatest Decrease in Profits: {months[maxdecrease_month]} (${maxdecrease})')





