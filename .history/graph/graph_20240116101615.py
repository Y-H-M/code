import csv

ipt=[]
opt=[]

with open('data.csv', mode="r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        ipt.append(row)
        
ipt.append(['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'])
    
for y in range(21)[2:]:
    for i in range(len(ipt)-1):
        ipt[i][y] = (float(ipt[i-1][y-1])+float(ipt[i+1][y-1]))/2

for row in ipt:
    print(row)

with open('data.csv', mode="w", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile, delimiter=',', encoding=)
    for row in reader:
        ipt.append(row)