import os

my_dir="/home/sony/ptrain/"
#intro to os.walk
print("*****************Start Print*********************")
for root_dir_path, sub_dirs, files in os.walk(my_dir):
	print ("Root Directory Path:",root_dir_path)
	print("sub directories",sub_dirs)
	print("Files",files)
	print("*"*25)
print("****************************")
