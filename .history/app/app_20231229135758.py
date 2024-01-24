"""App that checks on user daily"""

from datetime import date as d
import csv

date = d.today().strftime('%d/%m/%Y')
print("Today's date is:", date)

with open('app/data.csv', mode='r', encoding='utf-8') as csv_data:
    data = csv.DictReader(csv_data, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    print(f'Processed {line_count} lines.')