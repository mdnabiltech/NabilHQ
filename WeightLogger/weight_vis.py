import csv
import os
from datetime import date, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

fname = "weight_log.csv"

#Function that engages with user to collect data
def call_log():
    while True:
        day_status = input("Are you logging your weight for today? (y/n): ")

        if day_status == "y":
            day = (date.today()).strftime("%Y-%m-%d")
            weight = input("What is your weight today (lbs): ")
        else:
            day = input("What day do you want to log [YYYY-MM-DD]: ")
            weight = input("What was your weight on that day: ")
        
        log(day, weight)
        
        print()
        
        log_status = input("Do you want to log anymore days? (y/n) ")
        
        if log_status == "n":
            break
        print()

#Function to log into a csv
def log(date, weight): 
    if not os.path.exists(fname):
        with open(fname, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Weight"])
   
    with open(fname, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, weight])

#Function to visualize the data (using matplotlib)
def visualize():
    dates = []
    weights = []

    #reads through csv and sets up dates and weights lists
    with open(fname, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(datetime.strptime(row["Date"], "%Y-%m-%d"))
            weights.append(float(row["Weight"]))
    
    #sorts data by stitching together corresponding values then sorting
    sorted_data = sorted(zip(dates, weights))
    dates, weights = zip(*sorted_data)
    
    #Makes line graph
    plt.plot(dates, weights, marker = "o", color = "teal")
    plt.title("Weight Loss Journey")
    plt.xlabel("Date")
    plt.ylabel("Weight (lbs)")
    plt.grid(True)
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))  # e.g., Oct 01
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())  # auto space ticks
    plt.gcf().autofmt_xdate()  # rotate dates nicely
    plt.tight_layout()
    plt.show()

order = input("Hello Mr. Nabil, would you like to log a new entry or see you progress visualized? (l/v) ")

if order == "l":
    call_log()
elif order == "v":
    visualize()

