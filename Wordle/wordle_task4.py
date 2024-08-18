#initiate the list to stpre the dictionary
words_list = []

#input the first word
word = input().upper()

#input the guess the user makes
guess = input().upper()


#variable to iterate the characters on the guess word
char_cnt = 0

#variable to keep track of letters in the correct postion
cnt_right_pos = 0

#variable to keep track of letters in the wrong postion
cnt_wrong_pos = 0


#iterate through the word
for i in word:
    #check if the letters match in the same positions
    if i == guess[char_cnt]:
        #if the words match, increment the count
        cnt_right_pos += 1
        #move to the next character in the word
        char_cnt += 1
    else:
        #check if the guess has the letter in the word but in the wrong position
        for j in guess:
            #if letter exist in both but not in the same position
            if i == j:
                #increment the counter
                cnt_wrong_pos += 1
        #move to the next character in the word
        char_cnt += 1

#print the variables
print(cnt_right_pos)
print(cnt_wrong_pos)
