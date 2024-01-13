import random

def game():
    l = ['snake', 'water', 'gun']
    choose = random.choice(l)
    # print(choose)
    n=input('What do you chose?(Snake,Water or Gun)\n')
    if choose=='snake':
        d={'snake':'Draw!','water':'Snake drank the water.Computer Wins!👏','gun':'Gun killed the Snake.You Won!👏'}
        try:
            print(f'Computer Choosed {choose}')
            print(d[n.lower()])
            again(game)
        except KeyError:
            print('You have to choose out of the given choices.')
            game()
    elif choose=='water':
        d={'snake':'Snake drank the water.You Win!👏','gun':'Gun sank in water.Computer Wins!👏','water':'Draw'}
        try:
            print(f'Computer Choosed {choose}')
            print(d[n.lower()])
            again(game)
        except KeyError:
            print('You have to choose out of the given choices.')
            game()
    else:
        d={'snake':'Gun killed the Snake.You Win!👏','water':'Gun drowned in the Water.Computer Wins!👏','gun':'Draw!'}
        try:
            print(f'Computer Choosed {choose}')
            print(d[n.lower()])
            again(game)
        except KeyError:
            print('You have to choose out of the given choices.')
            game()
def again(func):
    ask=input('Do you want to play again?\n')
    if ask.lower()=='yes':
        func()
    elif ask.lower()=='no':
        print('Thank You.')


game()