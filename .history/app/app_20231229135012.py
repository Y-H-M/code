"""App that checks on user daily"""

from datetime import date
import csv

date = date.today().strftime("%d/%m/%Y")
print("Today's date is:", date.today().strftime("%d/%m/%Y"))

with open('data.csv') as data:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')