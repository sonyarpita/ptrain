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
#calculating future dates
#for one year 
future_date_after_1yr=current_date_time + timedelta(days=365)
#for 4 days and time 
future_date_after_4days=current_date_time + timedelta(days=4, hours=5, minutes=4, seconds=54)
# print calculated furture dates 
print("future date after 1 year", future_date_after_1yr)
print("future date after 4 days", future_date_after_4days)
print("Type:", type(future_date_after_4days))
#convert string
future_date_after_1yr_str=str(future_date_after_1yr)
future_date_after_4days_str=str(future_date_after_4days)
print("future date after 1 year", future_date_after_1yr_str)
print("future date after 4 days", future_date_after_4days_str)
print("Type:", type(future_date_after_4days_str))


