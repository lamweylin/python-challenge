import os
import csv

cwkdir = os.getcwd()
filepath = os.path.join(cwkdir, 'Resources', budget_data.csv)
month_count = 0
total = 0
prevalue = 0
diff = 0
diff_max = 0
diff_mix = 0

with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)

    for i in csvreader:
        month = i[0]
        amount = i[1]
        iamount = int(amount)
        diff = iamount - prevalue

        if diff_max < diff:
            diff_max = diff
            max_date = month
        if diff_mix > diff:
            diff_min = diff
            min_date = month
        prevalue = iamount
        month_count = month_count + 1
        total += int(amount)

print(f'Total Months : {month_count}')
print(f'Total: $ {total}')
print(f'Greatest Increase in Profits: {diff_max} : ($ {diff_max})')
print(f'Greatest Decrease in Profits: {diff_min} : ($ {diff_min})')