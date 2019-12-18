import sys
print("Enter a number")
x=int(sys.stdin.readline())
print(x)
sys.stdout.write("This is stdout text:%d \n"%(x))
sys.stderr.write("This is std err\n")
