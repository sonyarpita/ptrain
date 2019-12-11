user_list=list(input("Enter word/sentence: "))
for i in range(len(user_list)):
	if ord(user_list[i])==32 and ord(user_list[i+1])>96:
		asci=ord(user_list[i+1])-32
		user_list[i+1]=chr(asci)
str=''.join(user_list)
print("Evaluated Sentence: ",str)
