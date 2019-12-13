#use subprocess.run or subprocess.call
import os
import subprocess
import shlex

def run_cmd(cmd):
        args = shlex.split(cmd)
        res=subprocess.Popen(args,stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
        cmd_result=res.stdout.readlines()
        return cmd_result

os.system("ip -o link | grep 08:00 | awk \'{ print $2\" : \"$17 }\' > /tmp/interf.txt")
f_obj=open("/tmp/interf.txt")
if_list=[]
content=f_obj.readlines
for line in content():
    #print(line)
    conv_list=line.split(': ')
    if_list.append(conv_list[0])
print(if_list)
for i in range(len(if_list)):
	print(if_list[i])
    #subprocess.call()
	assign_ip="sudo ifconfig %s 102.1.1.96/24"%(if_list[i])
	print(assign_ip)
    #e=run_cmd(assign_ip)
	os.system(assign_ip)
	#print(e)
    #run_cmd(ifconfig if_list[i])

'''import os
cmd='ifconfig | grep 07:43 -B1'
os.system(cmd)
'''

'''import subprocess
output = subprocess.getoutput("ip -o link | grep 07:43 | awk \'{ print $2\" : \"$17 }\'")
print(output)
list=output.split(" ")
print("List:",list)
#print (output.split())
'''
'''
import os
os.system("ps > redirect.txt")
f_obj=open("redirect.txt")
pid_list=[]
content=f_obj.readlines()
flag=False
for line in content:
    if flag: #taking the flag to skip the first entry, bcz name of the fields
        string=''.join(line.split())#Creating as a string with single space everyword
        conv_list=string.split(' ')#converting the string to a list
        print(conv_list)#individual list
        pid_list.append(conv_list[0])#adding all PID to list
    flag=True
print(pid_list)
'''



