"""App that checks on user daily"""

from datetime import date
import csv

date = date.today().strftime("%d/%m/%Y")
print("Today's date is:", date.today().strftime("%d/%m/%Y"))

with open('data.csv') as data:
    csv_reader = csv.reader(csv_file, delimiter=',')