import subprocess 
subprocess.call(["ls", "-l", "/etc/resolv.conf"])
#OR
subprocess.call("ls -l /etc/resolv.conf", shell=True)
subprocess.call("date")
