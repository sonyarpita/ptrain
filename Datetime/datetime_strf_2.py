#strftime method is used to convert datetime as string format 
from datetime import datetime
timestamp=1528797322
date_time=datetime.fromtimestamp(timestamp)
print("date and time: ", date_time)
d=date_time.strftime("%m/%d/%Y, %H:%M:%S")
print("Output 2:", d)
d=date_time.strftime("%d %b, %Y")
print("Output 3:", d)

d=date_time.strftime("%d %B, %Y")
print("Output 4:", d)

d=date_time.strftime("%I%p")
print("Output 5:", d)

