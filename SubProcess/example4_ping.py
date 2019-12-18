# poll() function checks return code of the process, It will return None while the process is still running. 
# to get output, you can use process.stdout.readline() to read a single line. 
# conversely, when you use process.stdout.readlines(), it reads all lines and it also waits fo the process to finish is i has not finished yet

import subprocess
process=subprocess.Popen(["ping", "-c2", "python.org"], stdout=subprocess.PIPE, universal_newlines=True)
#OR
process1=subprocess.Popen("ping -c4 python.org", shell=True, stdout=subprocess.PIPE, universal_newlines=True)

while True:
	#output=process.stdout.readline()
	for output in process.stdout.readlines():
		print(output)
	#Do something else
	return_code = process.poll()
	if return_code is not None:
		print("Return code", return_code)
		#process has finished, read rest of the output
		for output in process.stdout.readlines():
			print(output)
		break
