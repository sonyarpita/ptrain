# we set stderr and stdout to subprocess.PIPE. This is a special value that indicates to subprocess.PIPE that a pipe should be open that you can then read with the communicate() functions. When you run communicate, it will wait until process is complete

import subprocess
import time
p=subprocess.Popen(["ping", "-c4","python.org"], stdout=subprocess.PIPE)
psd=subprocess.Popen(["ping", "-c4","1.1.1.1"], stdout=subprocess.PIPE)
output, err = p.communicate()
print(output)
f_obj=open('text.txt','w')
process=subprocess.Popen(["ls", "-l"], stdout=f_obj)
time.sleep(5)
fr_obj=open("text.txt","r")
print(fr_obj.read())
