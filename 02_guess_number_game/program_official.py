import random

print('---------------------------------')
print('     GUESS THAT NUMBER GAME')
print('---------------------------------')
print()

the_number = random.randint(0, 100)

name = input('Player, what is your name? ')

guess = -1
while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {}, your guess of {} was too LOW.'.format(name, guess))
        print('Sorry {}, your guess of {} was too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH.'.format(name, guess))
    else:
        print('Excellent work {}, you won! It was {}.'.format(name, guess))

print('Done')