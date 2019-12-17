# files are not created until open(filename) is called. Make sure all the subdirs exist beforehand
import os 
path="/home"
print(os.path.join(path,"/sony", "file.txt"))
path="/home/Sony/User"
print(os.path.join(path, "Documents", "file2.txt"))
path="/home"
print(os.path.join(path, "sony", "file3.txt", "ptrain"))
print(">>>>",path)
