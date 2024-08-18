import random

def load_the_dict(words_dict):

    """
    read_in_dict eads in the dictionary of words to use in the comparisons with the guesses
    from the users
        
    parameter words_dict: stores the words in the list to be used for the words dictionary
    returns: the dictionary of words stored in the list
     
    """
    

    with open('5_letter_words.txt', 'r') as file:
        words_dict = file.read().splitlines()
    
    """word = input().upper() #input the first word

    #input the words until user enters '###'
    while word != '###':
        words_list.append(word)
        word = input().upper()"""
        
    return words_dict


def reset_variables(char_cnt, cnt_right_pos, cnt_wrong_pos, prev_cnt_wrong_pos, result):
    """
    rest_variables takes in the varioud variables used in the program and sets them to the initial state
    """
    char_cnt = 0 #iterate through the dictionary word
    cnt_right_pos = 0 #count the number of letter in same positions
    cnt_wrong_pos = 0 #count the number of letter not in same positions
    prev_cnt_wrong_pos = 0 #save the previous value
    result = ['.'] *5 #list to capture the results

def start_game(play):
    
    play_game = input("Are you ready to start the game? (Y/N): ").upper()

    #Ensure the correct option is selected to start the game
    while play_game != 'N' and play_game != 'Y':
        print('ERROR: Please enter a valid response ')
        play_game = input("Are you ready to start the game? (Y/N): ").upper()


    #   Set the go_on variable to True to start the game
    if play_game == 'Y':
        play = True

    return play

def wrong_position(word, guess, guess_index, result_word, result_index):
    
    for j in word:
        if j == guess_index:
        #check if letter has a duplicate in the dict word
            if word.count(j)>1:
                #get the index and the letter thats duplicated
                for index, elmnt in enumerate(word): 
                    if elmnt == j:
                        #if the duplicated letter in word is at the position where the guess has the same letter
                        if guess[index] == word[index]: 
                            result_word[index] = j
                        else:
                            if result_word[result_index].islower() or result_word[result_index] ==".":
                                result_word[result_index] = j.lower()
                #cnt_wrong_pos += 1
            #if the letter is duplicated in the guess, check if it has been used already, else set the position with lowercase  
            elif guess.count(guess_index)>1:
                print('letter duplicated in guess')
                for index, elmnt in enumerate(guess):
                    if guess[index] == i and result_word[index].islower():
                        result_word[index] = j.lower()
                    else:
                        result_word[index] == "."
                        #encounted += 1

            else:
                if result_word[result_index].islower() or result_word[result_index] ==".":
                    result_word[result_index] = j.lower()
                #cnt_wrong_pos += 1
                #encounted += 1

    return result_word

    
char_cnt = 0
cnt_right_pos = 0
cnt_wrong_pos = 0
prev_cnt_wrong_pos = 0
result = ['.'] * 5

guessed_word_comp = ""


words_list = []
words_list = load_the_dict(words_list)

#Print the welcome message and instructions for the game
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n")
print("WELCOME TO THE WORDLE GAME!\n\n")
print("Aim of the game: Guess the hidden 5 letter english word in 6 tries \n\n\
      Instructions: \n \
       - Start by entering any 5 letter english word\n\
       - If you want to exit the game enter: 'Exit GAME'\n\
       - If your guess is correct, you win the game\n\
       - If your guess is incorrect: \n\
              - The letters that are in the hidden word and are in the right positions will be shown in capital letters\n\
              - The letters that are in the hidden word and are in the wrong positions will be shown in lower case letters\n\n")


go_on = False

go_on = start_game(go_on)

word = random.choice(words_list).upper() #pull random word from dictionary


try_count = 1 #initiate the try counter

#guess = input(f'Try {try_count}: Please enter a 5-letter guess word: ').upper()
guess = input(f'Try {try_count}: ').upper()
if guess == 'EXIT GAME':
    print(f'Thank you for playing the game! Hope to see you back again')
    print(f'The word was ', word)
    go_on = False

    


while go_on and try_count < 6:   
    #read in the guess word and ensure it is a 5-letter word
    
    try_count +=1  #increment the tries
    while guess != 'EXIT GAME' and (len(guess) > 5 or len(guess) < 5):
        print('ERROR: Your guess is not a 5-letter word.\n')
        #guess = input(f'Try {try_count}: Please enter a 5-letter guess word: ').upper()
        guess = input(f'Try {try_count}: ').upper()

    encounted = 0
    char_cnt = 0
    #iterate through the characters of the guess word, comparing them to the dictionary word
    for i in guess:
        """
        Checks if the letters match in the same positions
        If the character in guess word is same as the character in the dictionary word, add that
        letter (in caps) to the result list.
        """
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
                result = wrong_position(word, guess, i, result, char_cnt)
                '''for j in word:
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
                            print('letter duplicated in guess')
                            for index, elmnt in enumerate(guess):
                                if guess[index] == i and encounted > 0 and result[index].islower():
                                    result[index] = j.lower()
                                else:
                                    result[index] == "."
                                    encounted += 1
          
                        else:
                            if result[char_cnt].islower() or result[char_cnt] ==".":
                                result[char_cnt] = j.lower()
                            cnt_wrong_pos += 1
                            encounted += 1  '''
                cnt_wrong_pos += 1            
                char_cnt += 1

        else:
            char_cnt += 1
           

    for l in result:
        print(l, end='')
        guessed_word_comp += l
    print(end='\n\n')
    
    
    #if you find the word correctly, reset the variables and exit the game
    if guessed_word_comp == word: #cnt_right_pos >= len(word):
        print(f'Congratulation! You have found the word {word} in {try_count} tries!')
        reset_variables(char_cnt, cnt_right_pos, cnt_wrong_pos, prev_cnt_wrong_pos, result)
        go_on = False    
    else:
        #guess = input(f'Try {try_count}: Please enter a 5-letter guess word: ').upper()
        guess = input(f'Try {try_count}: ').upper()
        if guess == 'EXIT GAME':
            print(f'Thank you for playing the game! Hope to see you back again')
            print(f'The word was ', word)
            go_on = False


if try_count >= 6:
    print("Sorry! You have run out of tries.")
    print("The correct word is ", word, "\n\n")

print('Thank you for playing, Good-bye!')

    
