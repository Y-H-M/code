import csv

ipt=[]
opt=[]

with open('data.csv', mode="r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        ipt.append(row)
        
ipt.append(['0','0','0','0','0','0','0'])
    
for y in range(7)[2:]:
    for i in range(len(ipt)-1):
        ipt[i][y] = int(ipt[i-1][y-1])+int(ipt[i+1][y-1]))
        print(i)

for row in ipt:
    print(row)
