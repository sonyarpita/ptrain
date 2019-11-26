a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
#res=a/b
#print("Result is: ",res)
try:
	res=a/b
	print("Result is: ",res)
except ZeroDivisionError:
	print("ZeroDivisionError is raising an exception")
print("After result")
