num=int(input("Enter a number"))
sumn=0
rem=0
while num:
	rem=num%10
	sumn=sumn+rem
	num=num//10
print("Sum of given number:",sumn)
