import csv
with open('data.csv', mode="w", encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print(reader)
    for row in reader.__str__:
        print(row)