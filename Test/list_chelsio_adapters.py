'''import os
cmd='ifconfig | grep 07:43 -B1'
os.system(cmd)
'''

import subprocess
output = subprocess.getoutput("ip -o link | grep 07:43 | awk \'{ print $2\" : \"$17 }\'")
print(output)
list=output.split(" ")
print("List:",list)
#print (output.split())




