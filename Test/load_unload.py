import subprocess
import time
subprocess.call("rm -rf /tmp/.X11-unix/X1",shell=True)
subprocess.call("vncserver -geometry 1920x1080 :1",shell=True)
print("Unloading chcr,iw_cxgb4 and cxgb4")
subprocess.call("rmmod iw_cxgb4 chcr cxgb4",shell=True)
#sh rm_drivers.sh
time.sleep(2)
subprocess.call("modprobe cxgb4",shell=True)
time.sleep(2)

#Write logic to assign IP to chelsio interface 
#sh assign.sh
#sh ipv6_assign.sh
subprocess.call("ifconfig enp4s0f4 102.1.1.79/24 && ifconfig enp4s0f4d1 102.2.2.79/24 && ip -6 addr add 1000::79/64 dev enp4s0f4 && ip -6 addr add 2000::79/64 dev enp4s0f4d1",shell=True )
output=subprocess.getoutput("ethtool -i enp4s0f4")
print(output)

out2=subprocess.getoutput("strings \/sys\/kernel\/debug\/cxgb4\/0000\\:04\\:00.4\/flash | grep -im2 chel")
print(out2)
#auditctl -e 0
#echo 1 > /proc/sys/kernel/ftrace_dump_on_oops
