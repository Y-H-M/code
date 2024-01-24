import csv

ipt=[]
opt=[]

with open('data.csv', mode="r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        ipt.append(row)

for y in range(7)[2:]:
    for i in len(ipt):
        row[y] = row[y-1]

for row in ipt:
    print(row)
