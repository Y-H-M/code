import csv

ori=[]


with open('data.csv', mode="r", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        e