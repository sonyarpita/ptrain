import os
abspath=os.path.abspath("os_methods.py")
print(abspath)
file=os.path.basename("/home/sony/ptrain/os_methods.py")
print(file)
dirname=os.path.dirname("../../../")
print(dirname)
isexist=os.path.exists(dirname)
print(isexist)
full_path=os.path.expanduser("~")
print(full_path)
isfile=os.path.isfile(abspath)
print(isfile)
isDir=os.path.isdir(dirname)
print(isDir)
isAbs=os.path.isabs(dirname)
print(isAbs)
