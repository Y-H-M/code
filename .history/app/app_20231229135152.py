"""App that checks on user daily"""

from datetime import date
import csv

date = date.today().strftime("%d/%m/%Y")
print("Today's date is:", date.today().strftime("%d/%m/%Y"))

with open('data.csv') as data:
    csv_reader = csv.reader(data, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if not line_count:
            print(row)
            line_count += 1
        else:
            print('\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')