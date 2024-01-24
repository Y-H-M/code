"""App that checks on user daily"""

from datetime import date as d
import csv

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
    with open('app/data.csv', mode='r+', encoding='utf-8') as  csv_data:
        date, mood, productivity, good, workout = ask()
        writer = csv.writer(csv_data)
        row = [date, mood, productivity, good, workout]
        print(row)
        writer.writerow(row())
        
        
def ask():
    date = d.today().strftime('%d/%m/%Y')
    print("Today's date is:", date)
    mood = input('Mood: ')
    productivity = input('Productivity: ')
    good = input('Good: ')
    workout = input('Workout: ')
    return date, mood, productivity, good, workout


main()