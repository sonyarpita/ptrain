#Timedelta function demo
from datetime import datetime, timedelta
#timedelta has 3 attributes
print("Max:", timedelta.max) #the most positive timedelta object, timedelta(days=999999999,hours=23),minues=59,seconds=59,microseconds=999999)
print("Min:", timedelta.min) #the most negative timedelta bject,timedelta(-999999999)
print("Resolution:", timedelta.resolution) #the smallest psossible differnce between non-equal timedelta objects, timedelta(microseconds=1)

#using current time 
current_date_time=datetime.now()
#printing initial date
print("initial_date", current_date_time)
#calculating past dates
#for one year 
past_date_before_1yr=current_date_time - timedelta(days=365)
#for 4 days and time 
past_date_before_4days=current_date_time - timedelta(days=4, hours=5, minutes=4, seconds=54)
# print calculated furture dates 
print("past date before 1 year", past_date_before_1yr)
print("past date before 4 days", past_date_before_4days)
print("Type:", type(past_date_before_4days))
#convert string
past_date_before_1yr_str=str(past_date_before_1yr)
past_date_before_4days_str=str(past_date_before_4days)
print("past date before 1 year", past_date_before_1yr_str)
print("past date before 4 days", past_date_before_4days_str)
print("Type:", type(past_date_before_4days_str))


