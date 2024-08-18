#initiate the list to stpre the dictionary
words_list = []

#input the first word
word = input().upper()

#input the words until user enters '###'
while word != '###':
    if len(word) == 5: #strictly store only 5 letter words
        words_list.append(word)
    word = input().upper()

#print the lenght of the list which actually is the number of words in the dictionary
print(len(words_list))
