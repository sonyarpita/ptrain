a=int(input("Enter a number to determine if its prime or not: "))
b=a+1
counter=0
for i in range(1,b):
	if a%i == 0:
		counter=counter+1
if counter == 2:
	print("Number entered is a prime number")
else:
	print("Number entered is composite")
