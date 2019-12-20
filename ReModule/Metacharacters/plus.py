import re 
str = "The raix in Spain maui falls mainly in the plain!"
#Check if the string contains "ai" followed by 1 or more "x" characters 
x=re.findall("aix+",str)
print(x)
if (x):
    print("match")
else:
    print("No Match")
