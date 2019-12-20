import re 
#str = "The stays rain in Spain maui falls mainly in the plain!"
str="axz cacxz ccacxz"
#Check if the string contains "falls" or "stays"  
x=re.findall("(a|b|c)xz",str)
print(x)
if (x):
    print("match")
else:
    print("No Match")
