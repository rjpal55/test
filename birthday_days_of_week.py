
import datetime
from dateutil.relativedelta import relativedelta

curyear = str(2022)
curyearint = 2022

birthday = input("enter birthday in mm/dd/yyyy:" )

month,day,year = birthday.split('/')
month = month.replace("'","")
day = day.replace("'","")
birthday_this_year_tuple = (month, day, curyear)
birthday_this_year = ''

for item in birthday_this_year_tuple:
    birthday_this_year = birthday_this_year + item + '/'
    bty = birthday_this_year[:-1]
birthday_this_year = datetime.datetime.strptime(bty, "%m/%d/%Y")

while curyearint >= 2013:
    print(f"In", birthday_this_year.strftime("%Y"), "your birthday is on a", birthday_this_year.strftime("%A"))
    curyearint = curyearint - 1
    birthday_this_year = birthday_this_year - relativedelta(years=1)
