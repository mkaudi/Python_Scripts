user1 = str(input())
user2 = str(input())

if user1 == user2:
    print('Tie')
elif user1 == 'rock':
    if user2 == 'scissors':
        print('Player 1 wins')
    else:
        print('Player 2 wins')
elif user1 == 'paper':
    if user2 == 'rock':
        print('Player 1 wins')
    else:
        print('Player 2 wins')
elif user1 == 'scissors':
    if user2 == 'paper':
        print('Player 1 wins')
    else:
        print('Player 2 wins')
