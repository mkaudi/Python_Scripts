import random


def generate_number(end_num):
    '''
    Generates a random number from 0 to num
    :return: a random number between 0 and num
    '''

    return random.randint(0,end_num)

def number_check(guess, target):
    '''
    Check if the guessed number if higher or lower than the target number
    :param num: guessed number
    :param target: the number the user is trying to guess
    :return: indication on whether the guess is higher or lower than the target
    '''
    if target < guess:
        print("Your guess is higher than target")
    elif target > guess:
        print("Your guess is lower than target")
    else:
        print(f"Well done! Your guess {num} is correct")
        return False

    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    end_number = int(input("Please enter the end number: "))
    num = int(input("\nPlease enter a guess: "))
    target = generate_number(end_number)

    while number_check(num, target):
        num = int(input("\nPlease try again: "))

