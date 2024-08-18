#initiate the list to stpre the dictionary
words_list = []

#input the first word
word = input().upper()

#input the guess word
guess = input().upper()

#variable to iterate the characters on the guess word
char_cnt = 0

#variable to count the number of words in the correct postion
cnt = 0


#iterate through the word comparing with the guess characters with the word
for i in word:
    if i == guess[char_cnt]:
        cnt += 1
        char_cnt += 1
    else:
        char_cnt += 1

#print the number of letters in the correct position
print(cnt)
