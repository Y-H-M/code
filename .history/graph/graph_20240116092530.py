import csv
with open('data.csv', mode="r", encoding="utf-8") as csvfile:
    reader = csv.DictReaderreader(csvfile, delimiter=',')
    for row in reader:
        print(row)