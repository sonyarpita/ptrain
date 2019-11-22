start=int(input("Enter start of the range of 1000 numbers"))
stop=int(input("Enter end of the range of 1000 numbers"))
diff=stop-start
counter=0
if diff==1000:
    for num in range(start,stop):
        for j in (1,num+1):
            modulo=num%j
            if modulo==0:
                counter=counter+1
        if counter==2:
            print("Even numbers in the range->",start,"-",stop,"=",num)
else:
    print("Please enter a valid range")

