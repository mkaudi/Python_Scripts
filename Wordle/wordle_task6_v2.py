words_list = []

#read in the dictionary
word = input().upper() 


#read in the guess word
guess = input().upper()

guess_dict = {}
word_dict = {}

#count of each letter occurence on both word and guess
for l in guess:
    guess_dict[l] = guess.count(l)

for w in word:
    word_dict[w] = word.count(w)


#iterate through the dictionary word
char_cnt = 0

#count the number of letter in same positions
cnt_right_pos = 0

#count the number of letter not in same positions
cnt_wrong_pos = 0

#save the previous vale
prev_cnt_wrong_pos = 0

#list to capture the results
result = ['.'] *5

encounted = 0

#iterate through the characters of the guess word, comparing them to the dictionary word
for i in guess:
    """
    Checks if the letters match in the same positions
    If the character in guess word is same as the character in the dictionary word, add that
    letter (in caps) to the result list.
    """
    #result = ['.'] *5
    if char_cnt < 5 and (result[char_cnt] == "." or result[char_cnt].islower()):
        if  i == word[char_cnt]:
            result[char_cnt] = i
            cnt_right_pos += 1
            char_cnt += 1
            
        else:
            """
            check if the guess has the letter in the word but in the wrong position.
            Iterate through the dictionary word, if a character is also in the guess word,
            increment the variable and add that letter to the result list in lowercase.
            """
            for j in word:
                if j == i:
                    #check if letter has a duplicate in the dict word
                    if word.count(j)>1:
                        #get the index and the letter thats duplicated
                        for index, elmnt in enumerate(word): 

                            if elmnt == j:
                                #if the duplicated letter in word is at the position where the guess has the same letter
                                if guess[index] == word[index]: 
                                    result[index] = j
                                else:
                                    if result[char_cnt].islower() or result[char_cnt] ==".":
                                        result[char_cnt] = j.lower()
                        cnt_wrong_pos += 1
                    #if the letter is duplicated in the guess, check if it has been used already, else set the position with lowercase  
                    elif guess.count(i)>1: 
                        for index, elmnt in enumerate(guess):
                            if guess[index] == i and guess_dict[elmnt] > word_dict[i] and result[index].islower():
                                result[index] = j.lower()
                                if guess_dict[elmnt] > 0:
                                    guess_dict[elmnt] -= 1
                                if word_dict[j] == 1:
                                    guess_dict[elmnt] = 1
                            else:
                                result[index] == "."
     
                    else:
                        if result[char_cnt].islower() or result[char_cnt] ==".":
                            result[char_cnt] = j.lower()
                        cnt_wrong_pos += 1

                
            char_cnt += 1

    else:
        char_cnt += 1
           

for l in result:
    print(l, end='')
