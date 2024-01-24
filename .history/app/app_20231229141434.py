"""App that checks on user daily"""

from datetime import date as d
import csv

DATE = d.today().strftime('%d/%m/%Y')
print("Today's date is:", DATE)

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
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            print(row)
            line_count += 1
            
            
def write():
    with open('app/data.csv', mode='w', encoding='utf-8') as  csv_data:
        day, mood, productivity, good, workout = ask()
        fieldnames = ['day', 'mood', 'productivity', 'good', 'workout']
        writer = csv.DictWriter(csv_data, fieldnames=fieldnames)
        writer.writerow({day:day, mood:mood, productivity:productivity, good:good, workout: workout})
        
        
def ask():
    day = d.today().strftime('%d/%m/%Y')
    print("Today's date is:", day
    mood = input('Mood: ')
    productivity = input('Productivity: ')
    good = input('Good: ')
    workout = input('Workout: ')
    return day, mood, productivity, good, workout


main()