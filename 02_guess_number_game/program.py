import random

print('-' * 35)
print(' ' * 5, 'GUESS THE NUMBER APP')
print('-' * 35)

target = random.randint(0, 100)

prompt = 'Guess a number between 0 and 100: '
guess = int(input(prompt))

while guess != target:
    if guess > target:
        fail = 'Sorry but {} is GREATER than the number'.format(guess)
        print(fail)
    elif guess < target:
        fail = 'Sorry but {} is LOWER than the number'.format(guess)
        print(fail)
    guess = int(input(prompt))

success = 'YES! You\'ve got it. The number was {}'.format(target)
print(success)