import re 
str = "The rain in Spain maui falls mainly in the plain!"
#Check if the string contains "a" 2 times  
x=re.findall("a{2}",str)
print(x)
if (x):
    print("match")
else:
    print("No Match")
