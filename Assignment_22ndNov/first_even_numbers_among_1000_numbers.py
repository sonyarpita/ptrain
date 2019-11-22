start=int(input("Enter start of the range of 1000 numbers"))
stop=int(input("Enter end of the range of 1000 numbers"))
diff=stop-start
if diff==1000:
    for num in range(start,stop):
        modulo=num%2
        if modulo==0:
            print("Even numbers in the range->",start,"-",stop,"=",num)
else:
    print("Please enter a valid range")

