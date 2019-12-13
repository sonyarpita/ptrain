'''
Datetime is a module which is used to print the time and date 
Functions - 
now()- this functions is used to print current date and time 
strftime() - this method returns a string representing date and time using date, time or datetime object'''

import datetime
#To get current date and time 
datetime_object=datetime.datetime.now()
print("Current date and tme:", datetime_object)
#To get current date
date_object=datetime.date.today()
print("current date:", date_object)
#create custom date
custom_date=datetime.date(2019, 4,13)
print("custom date:", custom_date)
#get the date from timestamp 
timestamp=datetime.datetime.fromtimestamp(1326244364)
print("Datetime:", timestamp)
#get the year from date
today=datetime.date.today()
#get the year from date 
year=today.year
#get month
month=today.month
# get day
day=today.day
#display year,month, day
print("Current year", today.year)
print("Current year", today.month)
print("Current year", today.day)
#custom date creation
custom_date=datetime.date(2019,4,13)
print("custom_date", custom_date)
# get year
year=custom_date.year
month=custom_date.month
day=custom_date.day
print("Current year", custom_date.year)
print("Current year", custom_date.month)
print("Current year", custom_date.day)
custom_date_time=datetime.datetime(2017,11,28,23,55,59,342380)
print("Year=", custom_date_time.year)
print("Month=", custom_date_time.month)
print("day=",custom_date_time.day)
print("hour=", custom_date_time.hour)
print("minutes=", custom_date_time.minute)
print("seconds=", custom_date_time.second)
print("microseconds=", custom_date_time.microsecond)



