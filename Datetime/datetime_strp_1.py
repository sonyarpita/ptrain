#converts string format to datetime format 
from datetime import datetime
date_string="21 June 2018"
print("date_string = ", date_string)
print("type of date_string", type(date_string))
date_object=datetime.strptime(date_string, "%d %B %Y")
print("date_object=", date_object)
print("type of date object=", type(date_object))
