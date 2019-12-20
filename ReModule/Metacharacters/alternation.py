import re 
str = "The stays rain in Spain maui falls mainly in the plain!"
#Check if the string contains "falls" or "stays"  
x=re.findall("falls|stays",str)
print(x)
if (x):
    print("match")
else:
    print("No Match")
