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

        
    return words_dict


def reset_variables(char_cnt, cnt_right_pos, cnt_wrong_pos, result):
    """
    rest_variables takes in the varioud variables used in the program and sets them to the initial state
    """
    char_cnt = 0 #iterate through the dictionary word
    cnt_right_pos = 0 #count the number of letter in same positions
    cnt_wrong_pos = 0 #count the number of letter not in same positions
    result = ['.'] *5 #list to capture the results

def start_game(play):
    
    play_game = input("Are you ready to start the game? (Y/N): ").upper()

    #Ensure the correct option is selected to start the game
    while play_game != 'N' and play_game != 'Y':
        print('ERROR: Please enter a valid response ')
        play_game = input("Are you ready to start the game? (Y/N): ").upper()


    #Set the go_on variable to True to start the game
    if play_game == 'Y':
        play = True
    else:
        print('\nGoodbye! Hope to see you back again!\n')

    return play

def wrong_position(word, guess, guess_index, result_word, result_index, word_dict, guess_dict):

  
    for j in word:
        if j == guess_index:
        #check if letter has a duplicate in the dict word
            if word_dict[j] > 1:#.count(j)>1:
                #get the index and the letter thats duplicated
                for index, elmnt in enumerate(word): 
                    if elmnt == j:
                        #if the duplicated letter in word is at the position where the guess has the same letter
                        if guess[index] == word[index]: 
                            result_word[index] = j
                        else:
                            if (result_word[result_index].islower() or result_word[result_index] ==".") and word_dict[j] > 0:
                                result_word[result_index] = j.lower()

                                if word_dict[j] > 0:
                                    word_dict[j] -= 1

            #if the letter is duplicated in the guess, check if it has been used already, else set the position with lowercase  
            elif guess.count(guess_index)>1:

                for index, elmnt in enumerate(guess):
                    if guess[index] == guess_index and (guess_dict[elmnt] > word_dict[guess[index]] or result_word[index].islower()):
                        result_word[index] = j.lower()

                        if guess_dict[elmnt] > 0: 
                            guess_dict[elmnt] -= 1
                            
                        if word_dict[j] == 1:
                            guess_dict[elmnt] = 1
                    else:
                        result_word[index] == "."
                if word_dict[j] > 0:
                    word_dict[j] -= 1
 
            else:
                if (result_word[result_index].islower() or result_word[result_index] ==".") and word_dict[j] > 0:
                    result_word[result_index] = j.lower()
                    if word_dict[j] > 0:
                        word_dict[j] -= 1


    return result_word, word_dict


def print_result(result_word):
    print('\t', end='')
    for l in result_word:
        print(l, end='')
        result_string += l
    print(end='\n\n')

    return result_string


def next_try_check(word, result_string, try_count):

    #if you find the word correctly, reset the variables and exit the game
    if result_string == word: 
        print(f'Congratulation! You have found the word {word} in {try_count} tries!')
        return False    

    return True

def main():
    
    char_cnt = 0
    cnt_right_pos = 0
    cnt_wrong_pos = 0
    result_list = ['.'] * 5
    word_dict = {}
    guess_dict = {}

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
           - If you want to exit the game type: 'EXIT'\n\
           - If your guess is correct, you win the game\n\
           - If your guess is incorrect: \n\
                  - The letters that are in the hidden word and are in the right positions will be shown in capital letters\n\
                  - The letters that are in the hidden word and are in the wrong positions will be shown in lower case letters\n\n")


    go_on = False

    go_on = start_game(go_on)

    word = random.choice(words_list).upper() #pull random word from dictionary

    for w in word:
        word_dict[w] = word.count(w)
        
    try_count = 0 #initiate the try counter


    while go_on and try_count < 6:   
        #read in the guess word and ensure it is a 5-letter word
        try_count = try_count + 1
        guess = input(f'\nTry {try_count}/6: ').upper()
        if guess == 'EXIT':
            print(f'Thank you for playing the game! Hope to see you back again!')
            print(f'The word was \"', word,"\"")
            go_on = False
            
        elif len(guess) != 5:
            print('Your guess needs to be a 5 letter word. Try again.')
            
        else:
            
            #count of each letter occurence on both word and guess
            for l in guess:
                guess_dict[l] = guess.count(l)

            
            encounted = 0
            char_cnt = 0
            #iterate through the characters of the guess word, comparing them to the dictionary word
            for i in guess:
                """
                Checks if the letters match in the same positions
                If the character in guess word is same as the character in the dictionary word, add that
                letter (in caps) to the result list.
                """
                
                if char_cnt < 5 and (result_list[char_cnt] == "." or result_list[char_cnt].islower()):
                    if  i == word[char_cnt]:
                        if i.lower() in result_list:

                            #find the letter in the original result_list and replace it with an '.' if word_dict is 1 else -1
                            if result_list[result_list.index(i.lower())] == i.lower() and word_dict[i] == 0:
                                result_list[result_list.index(i.lower())] = '.'
                                
                            result_list[char_cnt] = i
                        else:
                            result_list[char_cnt] = i
                            
                        cnt_right_pos += 1
                        if word_dict[i] > 0:
                            word_dict[i] -= 1
                       
                    else:
                        """
                        check if the guess has the letter in the word but in the wrong position.
                        Iterate through the dictionary word, if a character is also in the guess word,
                        increment the variable and add that letter to the result list in lowercase.
                        """
                        result_list, word_dict = wrong_position(word, guess, i, result_list, char_cnt, word_dict, guess_dict)
                        cnt_wrong_pos += 1            

                    char_cnt += 1
                else:
                    char_cnt += 1
                   
            guess_word_comp = ''.join(result_list)
            print("------> ", guess_word_comp, end='\n')


            go_on = next_try_check(word, guess_word_comp, try_count)
        



    if try_count >= 6:
        print("\n\nSorry! You have run out of tries.")
        print("The correct word is \"", word, "\"\n\n")
        print('Thank you for playing, Good-bye!')

if __name__=="__main__":
    main()

    
