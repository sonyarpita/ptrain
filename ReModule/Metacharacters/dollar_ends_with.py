import re

str ="hello world hello world world hello sony hello come hello"
str1 = "world hello"

#check id the string starts with 'hello'

x=re.findall("hello$", str)
print(x)
y=re.findall("hello$", str1)
print(y)

if (x):
    print("yes, the string ends with hello")
else:
    print("No match")
