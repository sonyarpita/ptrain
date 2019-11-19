a=int(input("Enter number: "))
temp=0
if a==0:
	print("Number of digits=1")
else:
	while a>0:
		b=a%10
		a=a//10
		temp=temp+1
	print("Number of digits = ",temp)
