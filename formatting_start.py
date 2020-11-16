from datetime import datetime

def main():
    now = datetime.now()
    print(now.strftime("The current year is %Y"))
    print(now.strftime("%a, %d, %B, %y")) #day,date,month,year

    # date formatting
    # print(now.strftime("locale time:%X")) #locale time
    # print(now.strftime("locale date and time:%c")) #locale date and time
    # print(now.strftime("locale date:%x")) #locale date

    # Time formatting 
    print(now.strftime("CurrentTime : %I:%M:%S %p")) #p is for am and pm
    print(now.strftime("CurrentTime : %H:%M")) #24hr format


if __name__ == "__main__":
    main()