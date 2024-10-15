import random

magic_number = random.randint(1, 100)

print('Guess a number between 1 and 100')

number_of_guesses = 0
while True:
    guess = int(input('What is your next guess? '))
    number_of_guesses += 1

    if guess > magic_number:
        print('lower ...')

    elif guess < magic_number:
        print('higher ...')

    else:
        print('YEAAAH!!!! You guessed it in %d guesses' % number_of_guesses)
        break

