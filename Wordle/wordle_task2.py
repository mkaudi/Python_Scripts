#initiate the list to stpre the dictionary
words_list = []

#input the first word
word = input().upper()

#input the words until user enters '###'
while word != '###':
    if len(word) == 5: #strictly store only 5 letter words
        words_list.append(word)
    word = input().upper()

#input the guess the user makes
guess = input().upper()

#if the guess word is in the list or dictionary then print Valid else print Invalid
if guess in words_list:
    print("Valid")
else:
    print("Invalid")
        
