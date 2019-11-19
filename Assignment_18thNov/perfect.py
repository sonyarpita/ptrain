a=int(input("Enter a number to determine if its perfect or not: "))
original_a=a
counter=0
sum=0
for i in range(1,a):
	if a%i == 0:
		sum=sum+i		
if sum == original_a :
	print("Number entered is a perfect number")
else:
	print("Number entered is not a perfect number")
