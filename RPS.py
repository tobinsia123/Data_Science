count = 0  # total tries
count_1 = 0
count_2 = 0
y = ['Rock', 'Paper', 'Scissors']
x = int(input("How many games:"))

for i in range(x):
    player1 = input("Rock, Paper or Scissors:")
    player2 = input("Rock, Paper or Scissors:")
    count = count + 1

    if player1 or player2 not in y:
        print('invalid')
        count = count + 1
        break

    elif player1 == player2:
        print("Draw!")

    elif player1 == ('Rock'):
        if player2 == ('Paper'):
            count_2 = count_2 + 1
        if player2 == ('Scissors'):
            count_1 = count_1 + 1

    elif player1 == ('Paper'):
        if player2 == ('Rock'):
            count_1 = count_1 + 1
        if player2 == ('Scissors'):
            count_2 = count_2 + 1

    elif player1 == ('Scissors'):
        if player2 == ('Rock'):
            count_2 = count_2 + 1
        if player2 == ('Paper'):
            count_1 = count_1 + 1


    print('Game:', count)
    print('Player 1 score:', count_1)
    print('Player 2 score:', count_2)


