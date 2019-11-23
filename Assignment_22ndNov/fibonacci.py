limit=int(input("Enter limit of Fibonacci series: "))
i=0
j=0
prevj=1
for i1 in range(1,limit):
	if j<=limit:
		print(j,",",end="")
		j=i+prevj
		i=prevj
		prevj=j
print('\n')
	
