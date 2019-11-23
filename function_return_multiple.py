def calculator(a,b):
	add=a+b
	sub=a-b
	mul=a*b
	return add,sub,mul
a=int(input("Enter number"))
b=int(input("Enter number"))
add,sub,mul=calculator(a,b)
print("Addition is",add)
print("substraction is",sub)
print("multiplication is",mul)
