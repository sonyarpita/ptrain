start=int(input("Enter start of the range of 1000 numbers: "))
stop=int(input("Enter end of the range of 1000 numbers: "))
diff=stop-start
#counter=0
if diff==100:
	for num in range(start,stop):
		#print("Value of Number = ",num)
		counter=0
		for j in range(1,num+1):
		#print("Value of J = ",j)
			modulo=num%j
			if modulo==0:
				counter=counter+1
		print("Number of divisors of",num,"=",counter)
		if counter==2:
			print("Prime numbers in the range->",start,"-",stop,"=",num)
else:
    print("Please enter a valid range")
