import csv

ipt=[]
opt=[]

with open('data.csv', mode="r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        ipt.append(row)
        
ipt.append([2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    
for y in range(7)[2:]:
    for i in range(len(ipt)-1):
        ipt[i][y] = (float(ipt[i-1][y-1])+float(ipt[i+1][y-1]))/2
        print(i)

for row in ipt:
    print(row)
