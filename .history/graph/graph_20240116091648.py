import csv
with open('data.csv', mode="w") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print(reader)
    for row in reader:
        print(row)