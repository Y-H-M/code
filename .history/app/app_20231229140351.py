"""App that checks on user daily"""

from datetime import date as d
import csv

DATE = d.today().strftime('%d/%m/%Y')
print("Today's date is:", DATE)

def read():
    with open('app/data.csv', mode='r', encoding='utf-8') as csv_data:
        data = csv.DictReader(csv_data, delimiter=',')
        line_count = 0
        for row in data:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(row)
            line_count += 1
            
            
def write():
    with open('app/data.csv', mode='w', encoding='utf-8') as  csv_data:
        
        
def ask():
    day = DATE
    mood = input('')
            