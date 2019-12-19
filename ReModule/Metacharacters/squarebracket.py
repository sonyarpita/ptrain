import re 
str1="Hello Today I am going to learn regex module"
str2="Apple iPhone 11 Pro Max-Midnight-green 256GB price is 53535.38"
# Find all lower case characters alphabetically between a and m
x=re.findall("[abc]", str1)
print(x)
b=re.findall("[^abc]", str1)
print(b)
y=re.findall("[a-m]", str1)
print(y)
z=re.findall("[0-9]", str2)
print(z)
z=re.findall("[^6-9]", str2)
print(z)
a=re.findall("az", str2) #Thi is check the expression "az" not a and z as inidividual characters 
print(a)
