import csv

ipt=[]
opt=[]

with open('data.csv', mode="r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        ipt.append(row)
        
opt = ipt

for row in ipt:
    print(row)

for y in range(7)[2:]:
    for row in ipt:
        
