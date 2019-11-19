'''a=int(input("Enter number: ")) 
product=1
while a>0:
	b=a%10
	a=a//10
	#print("b=",b)
	product=product*b
print("Product=",product)'''

a=int(input("Enter number: "))
temp_of_a=a
temp=0
if temp_of_a==0:
        print("Number of digits=1")
else:
        while temp_of_a>0:
                b=temp_of_a%10
                temp_of_a=temp_of_a//10
                temp=temp+1
#        print("Number of digits = ",temp)
#power of
power=10**(temp-1)
#print("Power of 10=",power)
#print("Value of a",a)


reverse=0
while a>0:
	b=a%10
	a=a//10
	#print("b=",b)
	reverse=reverse+b*power
	#print("Interim reverse=",reverse)
	power=power//10        
print("Reverse of entered number=",reverse)




























