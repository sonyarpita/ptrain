import time
from threading import Thread

def eventhrd(x):
	print("Even thread")
	time.sleep(1)
	print("Even is",x)
def oddthrd(x):
	print("odd thread")
	time.sleep(1)
	print("Odd is",x)
th=Thread(target=eventhrd,args=(1,))
th.start()
th=Thread(target=oddthrd,args=(1,))
th.start()
