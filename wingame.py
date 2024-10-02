win_num=43
guess=1
number=int(input('Guess a number between 1 and 100:'))
game_over=False

while not game_over:
    if number==win_num:
        print(f'you win and guess the number')
        game_over=True
    else:
        if number < win_num:
            print('T(oo low')
            guess+=1
            number=int(input('Guess Again'))
        else:
            print('Too High')
            guess+=1
            number=int(input('Guess Again'))

     