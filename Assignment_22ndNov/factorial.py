a=int(input("Enter number to calculate factorial: "))
if a == 0:
    print("Enter non-zero number")
else:    
    product=1
    for i in range(1,a+1):
        product=product*i
    print("Factorial of",a,"=",product)
