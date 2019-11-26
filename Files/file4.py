f=open('samples.txt','w')
f.write('Hello world\n')
f.write('Hi how are you\n')
f.write('Sony arpita das\n')
f=open('samples.txt','r')
#content = f.readlines()
#for line in content:
for line in f.readlines():
	print(line)
