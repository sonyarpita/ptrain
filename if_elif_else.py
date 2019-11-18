'''
syntax:
if condition1:
	statements
elif condition2:
	statements
elif condition3:
	statements
--------------------
--------------------
--------------------
else:	
	statements
'''
a=int(input("Enter a first num"))
b=int(input("Enter a second num"))
c=int(input("Enter a third num"))
if a>b and a>c:
	print ("a is big:",a)
elif b>a and b>c:
	print ("b is big:",b)
elif c>a and c>b:
	print ("c is big:",c)
else:
	print("two or three nums are same")

