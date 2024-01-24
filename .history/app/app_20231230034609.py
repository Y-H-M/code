"""App that checks on user daily"""

from datetime import date as d
import csv
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.dates as mdates

def main():
    while True:
        action = input('Action (\u0332write/\u0332read): ')
        if action == 'w':
            write()
            break
        elif action == 'r':
            read()
            break
        else:
            print('??')

def read():
    with open('app/data.csv', mode='r', encoding='utf-8') as csv_data:
        data = csv.DictReader(csv_data, delimiter=',')
        line_count = 0
        for row in data:
            if line_count == 0:
                print(f'Date\t\tMood\tProductivity\tGood\tWorkout')
                line_count += 1
            print(f'{row["date"]}\t{row["mood"]}\t{row["productivity"]}\t{row["good"]}\t{row["workout"]}')
            line_count += 1
    plot()
            

def plot():
    with open('app/data.csv', mode='r', encoding='utf-8') as csv_data:
        x=[]
        yMood=[]
        yProd=[]
        data = csv.DictReader(csv_data, delimiter=',')
        for row in data:
            x.append(row['date'])
            yMood.append(int(row['mood']))
            yProd.append(int(row['productivity']))
        fig, ax = plt.subplots()
        ax.set_title('Mood + Productivity')
        ax.set_xlabel('Date')
        ax.set_ylabel('%')
        ax.set_ylim(0,100)
        ax.yaxis.set_major_locator(MultipleLocator(10))
        ax.plot(x, yMood, label='Mood', color='green', linestyle='solid')
        ax.plot(x, yProd, label='Productivity', color='blue', linestyle='solid')
        plt.rcParams["figure.autolayout"] = True
        plt.savefig('graph.png')
            
def write():
    with open('app/data.csv', mode='a', encoding='utf-8', newline='') as csv_data:
        # Check if the file is empty (no header)
        if csv_data.tell() == 0:
            header = ['date', 'mood', 'productivity', 'good', 'workout']
            csv.writer(csv_data).writerow(header)

        date, mood, productivity, good, workout = ask()
        print(f'date: {date}, mood: {mood}, productivity: {productivity}, good: {good}, workout: {workout}')

        row = {'date': date, 'mood': mood, 'productivity': productivity, 'good': good, 'workout': workout}
        print(row)

        writer = csv.DictWriter(csv_data, fieldnames=[key for key in row])
        writer.writerow(row)

def ask():
    date = d.today().strftime('%d/%m/%Y')
    print("Today's date is:", date)
    mood = input('Mood: ')
    productivity = input('Productivity: ')
    good = input('Good: ')
    workout = input('Workout: ')
    return date, mood, productivity, good, workout

main()