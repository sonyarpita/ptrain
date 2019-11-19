a=int(input("Enter number: ")) 
product=0
while a>0:
	b=a%10
	a=a//10
	product=product+b
print("Sum=",product)
