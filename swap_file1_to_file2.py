fa=open("a.txt","r")
fb=open("b.txt","r")
fc=open("c.txt","w+")
#print(fa.read())
print("------------------------------")
fa.seek(0,0)
for i in fa.readlines():
    #print(i)
    
    fc.write(i)

print(fc.read)
'''print(fa.tell())
for i in fb.readlines():
    print(i)
'''
    
