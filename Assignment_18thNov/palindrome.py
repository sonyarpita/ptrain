a=int(input("Enter number: "))
temp_of_a=a
original_a=a
temp=0
#Calculate number of digits
if temp_of_a==0:
        print("Number of digits=1")
else:
        while temp_of_a>0:
                b=temp_of_a%10
                temp_of_a=temp_of_a//10
                temp=temp+1
power=10**(temp-1)

#Reverse Number Logic
reverse=0
while a>0:
	b=a%10
	a=a//10
	reverse=reverse+b*power
	power=power//10        
#print("Reverse of entered number=",reverse)

#Check if palindrome 
if original_a==reverse:
	print("Entered number is a palindrome")
else:
	print("Entered number is not a palindrome")


























