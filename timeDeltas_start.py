from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

print(timedelta(days=365,hours=5,minutes=1))

now = datetime.now()
print(now)

print("One year from now: ", str(now+timedelta(days=365)))
# future date
print("in 2 days and 3 weeks it will be " + str(now + timedelta(days=2,weeks=3)))
# past date - 1 week ago
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d %Y")
print("One week ago , it was: ", s)

# how many days it is until next april fools date 
today= date.today()
afd = date(today.year,4,1) #april 1st
if (afd < today):
    print("April fools' day already passed by %d days ago" %((today-afd).days))
    afd = afd.replace(year = today.year+1)

time_to_afd = afd-today
print("Its just",time_to_afd.days,"days until April Fools' Day")

# Jun 30 , how many days until next bday 
# today=date.today()
# bday=date(today.year,6,30)
# diff=(bday-today).days
# if diff>0:
#   print("Birthday in %d days" % diff)
# else:
#   print("Birthday in %d days" % (diff+365))

# if __name__ == "__main__":
#     main()