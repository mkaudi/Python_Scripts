words_list = []

#read in the dictionary
word = input().upper() 

#read in the guess word
guess = input().upper()

#iterate through the dictionary word
char_cnt = 0

#count the number of letter in same positions
cnt_right_pos = 0

#count the number of letter not in same positions
cnt_wrong_pos = 0

#save the previous vale
prev_cnt_wrong_pos = 0

#list to capture the results
result = []

#iterate through the characters of the guess word, comparing them to the dictionary word
for i in guess:
    """
    Checks if the letters match in the same positions
    If the character in guess word is same as the character in the dictionary word, add that
    letter (in caps) to the result list.
    """
    if  i == word[char_cnt]:
        result.append(i)
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
                result.append(j.lower())
                cnt_wrong_pos += 1
        if prev_cnt_wrong_pos == cnt_wrong_pos:
            result.append('.')
            
        char_cnt += 1
        prev_cnt_wrong_pos = cnt_wrong_pos
        
for l in result:
    print(l, end='')
