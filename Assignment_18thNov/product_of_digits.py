a=int(input("Enter number: ")) 
product=1
if a==0:
	print("Product=",a)
else:
	while a>0:
		b=a%10
		a=a//10
		#print("b=",b)
		product=product*b
	print("Product=",product)
