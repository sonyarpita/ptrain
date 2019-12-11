user_word=input("Enter word: ")
vowel_list=['a','e','i','o','u']
counter=0
list_word=[]
list_word=list(user_word)
for vowel in range(len(vowel_list)):
    counter=0
    for i in range(len(user_word)):
        if vowel_list[vowel]==user_word[i]:
            counter+=1
    print(vowel_list[vowel],"occurs",counter)


'''   if vowel_list[vowel] in user_input :
        counter+=1
        if counter==1:
            print(vowel_list[vowel],"occurs",counter,"time")
        else:
            print(vowel_list[vowel],"occurs",counter,"times")
list_word=[]
list_word=list(user_input)
for i in range(len(list_word)):
    print(list_word[i])'''
