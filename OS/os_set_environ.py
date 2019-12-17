# Path variable is changed only inside this program. It reverts once the file exits
import os 
os.system("echo hello")
os.system("echo $XDG_SEAT")
os.environ["XDG_SEAT_PATH"]='qqrq'
os.system("echo After $CDG_SEAT_PATH")
