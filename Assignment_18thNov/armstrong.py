a=int(input("Enter number: ")) 
original_a=a
product=0
while a>0:
	b=a%10
	a=a//10
	product=product+b**3
#print("Sum=",product)
if original_a==product:
	print("Number entered thus far is armstrong")
else:
	print("Number entered is not armstrong")
