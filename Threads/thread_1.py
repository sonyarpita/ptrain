import time
from threading import Thread
def sleepFun(x):
	print("Thread",x,"is going to sleep for 2 seconds")
	time.sleep(2)
	print("Thread",x,"is active now")
th=Thread(target=sleepFun,args=(1, )) #args takes argument list for sleepFun function in this case.
th.start()
#sleepFun(1)
print("Hello I am executing parallel to thread")
