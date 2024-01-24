"""App that checks on user daily"""

from datetime import date as d
from datetime import datetime as dt
import csv
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator as ml
from matplotlib import dates as mdates
from PIL import Image as img
from prettytable import PrettyTable as pt


def main():
    """Main Function. Checks for the choice of action (Either Write or Read)"""
    while True:
        action = input("Action (\u0332write/\u0332read): ")
        if action == "w":
            write()
            break
        if action == "r":
            read()
            break
        print("??")


def read():
    """Read Function. Prints the csv out, then calls the plot function."""
    with open("app/data.csv", mode="r", encoding="utf-8") as csv_data:
        data = csv.DictReader(csv_data, delimiter=",")
        table = pt()
        table.field_names = ['Date', 'Mood', 'Productivity', 'Good', 'Workout']
        for row in data:
            table.add_row([row['date'], row['mood'], row['productivity'], row['good'], row['workout']])
        table.align = "l"
        print(table)
    plot()


def plot():
    """Plots all the data, then outputs images of the graphs"""
    with open("app/data.csv", mode="r", encoding="utf-8") as csv_data:
        # Line Graph
        dates = []
        y_mood = []
        y_productivity = []
        y_good, n_good = 0, 0
        y_workout, n_workout = 0, 0
        data = csv.DictReader(csv_data, delimiter=",")
        for row in data:
            dates.append(row["date"])
            y_mood.append(int(row["mood"]))
            y_productivity.append(int(row["productivity"]))
            if row["good"] == "y":
                y_good += 1
            else:
                n_good += 1
            if row["workout"] == "y":
                y_workout += 1
            else:
                n_workout += 1
        good = [y_good, n_good]
        workout = [y_workout, n_workout]
        x = [dt.strptime(date, "%d/%m/%Y") for date in dates]
        _, ax = plt.subplots(figsize=(max(6, len(x) * 0.1), 6))

        ax.set_title("Mood + Productivity")
        ax.set_xlabel("Date")
        ax.set_ylabel("%")
        ax.set_ylim(0, 100)
        ax.xaxis.set_major_locator(mdates.MonthLocator(bymonthday=[1, 15]))
        ax.yaxis.set_major_locator(ml(10))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m/%Y"))
        ax.plot(x, y_mood, label="Mood", color="green", linestyle="solid")
        ax.plot(x, y_productivity, label="Productivity", color="blue", linestyle="solid")
        plt.rcParams["figure.autolayout"] = True
        plt.savefig("Mood+Productivity.png")
        plt.close()

        plt.pie(good, labels=["y", "n"], autopct="%1.1f%%", startangle=90)
        plt.title("Good")
        plt.savefig("Good.png")
        plt.close()

        plt.pie(workout, labels=["y", "n"], autopct="%1.1f%%", startangle=90)
        plt.title("Workout")
        plt.savefig("Workout.png")
        plt.close()

        graphimg = img.open("Mood+Productivity.png")
        goodimg = img.open("Good.png")
        workoutimg = img.open("Workout.png")
        wgraphimg, hgraphimg = graphimg.size
        wgoodimg, hgoodimg = goodimg.size
        wworkoutimg, _ = workoutimg.size
        wtotalimg = max(wgraphimg, (wgoodimg + wworkoutimg))
        htotalimg = hgraphimg + hgoodimg
        totalimg = img.new("RGB", (wtotalimg, htotalimg), (255, 255, 255))
        totalimg.paste(graphimg, (0, 0))
        totalimg.paste(goodimg, (0, hgraphimg))
        totalimg.paste(workoutimg, (wgoodimg, hgraphimg))
        totalimg.save("DailyReport.png")
        graphimg.close()
        goodimg.close()
        workoutimg.close()


def write():
    """Calls ask() to get input from user, then updates the csv"""
    with open("app/data.csv", mode="a", encoding="utf-8", newline="") as csv_data:
        if csv_data.tell() == 0:
            header = ["date", "mood", "productivity", "good", "workout"]
            csv.writer(csv_data).writerow(header)
        date, mood, productivity, good, workout = ask()
        print(
            f"date: {date}, mood: {mood}, productivity: {productivity}, good: {good}, workout: {workout}"
        )
        row = {
            "date": date,
            "mood": mood,
            "productivity": productivity,
            "good": good,
            "workout": workout,
        }
        writer = csv.DictWriter(csv_data, fieldnames=[key for key in row])
        writer.writerow(row)


def ask():
    """Prompts the user for the information"""
    date = d.today().strftime("%d/%m/%Y")
    print("Today's date is:", date)
    mood = input("Mood: ")
    productivity = input("Productivity: ")
    good = input("Good: ")
    workout = input("Workout: ")
    return date, mood, productivity, good, workout


main()
