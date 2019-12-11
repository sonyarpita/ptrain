import time
from threading import Thread

def calculation():
	a=10
	b=20
	res=a+b
	return res
def sleepFun(x):
	print("Thread",x,"is going to sleep for  seconds")
	time.sleep(2)
	print("Thread",x,"is active now")
for i in range(10):
	th=Thread(target=sleepFun,args=(i,))
	th.start()
res=calculation()
print("Result= ",res)
