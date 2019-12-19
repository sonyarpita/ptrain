import re 
str = "hello world helo"
# search for a sequence that starts with "he", followed by two (any)characters, and an "o"
x=re.findall("he..o", str)
print(x)
x=re.findall("he...o", str)
print(x)
x=re.findall("he.o", str)
print(x)
