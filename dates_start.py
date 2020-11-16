from datetime import date
from datetime import time
from datetime import datetime

def main():
    # today = date.today()
    # print("Today's date =", today)
    # print("Date components: ", today.day, today.month, today.year)

    # print("Today's weekday number is ", today.weekday())
    # days = ["Mon", "Tue", "WEd","Thurs","Fri","Sat","Sun"]
    # print("which is a ", days[today.weekday()])
    today = datetime.now()
    print("Current date time is ", today)

    # get the current time 
    t = datetime.time(datetime.now())
    print("Current time is ",t)

if __name__ == "__main__":
    main()
