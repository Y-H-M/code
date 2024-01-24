import csv

ipt=[]
opt=[]

with open('data.csv', mode="r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        ipt.append(row)
        
ipt.append([0,0,0,0,0,0,0])

for y in range(7)[2:]:
    for i in range(len(ipt)):
        ipt[i][y] = ipt[i-1][y-1]+ipt[i+1][y-1]

for row in ipt:
    print(row)
