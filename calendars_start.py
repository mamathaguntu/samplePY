import calendar 

# create a plain text calendar
c = calendar.TextCalendar(calendar.MONDAY) #start day of the week in the calendar 
st = c.formatmonth(2017,12,0,0)
print(st)

# prints the following 

#    December 2017
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31

# html calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2017, 12)
# print(st)

# loop over the days in the month
# for i in hc.itermonthdays(2017,8):
    # print(i)
    # the zeroes at the start and the end of the output represents the days of the other month


# for name in calendar.month_name:
#     print(name)

# for day in calendar.day_name:
#     print(day)

# dates for the upcoming year, get first friday of each month for the meeting date 
print("Team meetings will be on: ")
for m in range(1,13):
    cal = calendar.monthcalendar(2018,m) # for the year 2018
    # get first 2 weeks to know which week has 1st friday
    week1 = cal[0] 
    week2 = cal[1]
    # decide which week has 1st friday
    if (week1[calendar.FRIDAY] != 0): # 0 means it is in another month
        meetday = week1[calendar.FRIDAY]
    else:
        meetday= week2[calendar.FRIDAY]
    # print the month and its first friday date 
    print("%10s %2d" % (calendar.month_name[m], meetday))