import os 
print("Get current OS name:", os.name)
print("Get current path", os.getcwd)
print(os.system('ls'))
print("get group id", os.getgid())
print("get user id", os.getuid())
print("get process id", os.getpid())
print("list all directoriess in path")
print(os.listdir('/home/sony/Sony'))
print("create new directory")
os.mkdir("/home/sony/Sony/dummy")
print("create new file")
os.mknod("my_fle.py")
print("get current env", os.environ.get('HOME'))
print("rename folder name")
print("list all directories in specifict path")
print(os.listdir("/home/sony/Sony"))
print("change directory")
os.chdir("/home/sony")
os.rename("/home/sony/Sony/my_fle.py", "/home/sony/Sony/my_file.py")
print("delete empty directory")
os.rmdir("/home/sony/Sony/dummy")
print("to create recursive directories")
os.makedirs('lev3/lev4')
print("delete recursive directoriies")
os.removedirs('lev3/lev4')
print("to delete file")
os.remove("my_file.py")
print("Stats f file", os.stat("os_get_environment.py"))