import time
import datetime
# The unix epoch (or unix time or posix time or unix timestamp) is the numer of seconds that have elapsed since January1, 1970
epoch_time_seconds=time.time()
print("Time in seconds snce the epoch:", epoch_time_seconds)
date_time=datetime.datetime.now()
current_time=date_time.time()
print("Hour:", current_time.hour)
print("Minutes:", current_time.minute)
print("Seconds:", current_time.second)
print("Micro seconds:", current_time.microsecond)
#create custom time 
empty_time=datetime.time()
print("empty time=", empty_time)
custom_time=datetime.time(11,34,56)
print("custom time=", custom_time)
custom_time_with_attributes=datetime.time(hour=11,minute=34,second=56)
print("custom time with attributes", custom_time_with_attributes)
custom_time_with_microseconds=datetime.time(11,34,56,234566)
print("custom time with microseconds", custom_time_with_microseconds)
print("Hour=", custom_time.hour)
print("Minutes=", custom_time.minute)
print("Seconds=", custom_time.second)
print("Microseconds=", custom_time.microsecond)
