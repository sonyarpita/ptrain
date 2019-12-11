user_word=input("Enter word: ")
vowel_list=['a','e','i','o','u']
list_word=list(user_word)
for vowel in range(len(vowel_list)):
    counter=0
    for i in range(len(user_word)):
        if vowel_list[vowel]==user_word[i]:
            counter+=1
    print(vowel_list[vowel],"occurs",counter)

