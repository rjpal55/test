# curyear = 2022
# yearcount = 10
# while yearcount > 0:
#     print(curyear)
#     curyear = curyear-1
#     yearcount = yearcount-1

# current date minus a year

import datetime
import calendar
from dateutil.relativedelta import relativedelta

# minus 1 year
birthday = input("enter birthday in mm/dd/yyyy:" )
yearcount = 0
while yearcount != 10:
    birthdaydate = datetime.datetime.strptime(birthday, "%m/%d/%Y")
    currentTimeDate = datetime.now() - relativedelta(years=yearcount)
    # print("Your birthday in", %Y, "is on a", calendar.day_name[birthdaydate.weekday()])
    currentTime = currentTimeDate.strftime('%Y')
    print(currentTime)
    yearcount = yearcount +1