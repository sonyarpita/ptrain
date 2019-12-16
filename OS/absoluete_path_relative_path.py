import os
abspath=os.path.abspath("file1.txt")#To get absoluete path of where the file exsists
print (abspath)
file=os.path.basename("/home/naveen/dummy1/testfolder/file1.txt") #To get file name
print(file)
dirname=os.path.dirname("/home/naveen/dummy1/testfolder")
#drirname=os.path.dirname("../../")
print(dirname)
isexists=os.path.exists(dirname)
print(isexists)
full_path=os.path.expanduser("~") #current full path
print(full_path)
isfile=os.path.isfile(abspath)
print(isfile)
isDir=os.path.isdir(dirname)
print(isDir)
isAbs=os.path.isabs(dirname)
print(isAbs)
