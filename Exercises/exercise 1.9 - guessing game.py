import random

lower = 1
upper = 100

magic_number = random.randint(lower, upper)

print(f'Guess a number between {lower} and {upper}.')
number_of_guesses = 0

while True:

    first_or_next = 'first' if number_of_guesses == 0 else 'next'
    guess = int(input(f'What is your {first_or_next} guess? '))

    number_of_guesses += 1

    if guess > magic_number:
        print('lower ...')

    elif guess < magic_number:
        print('higher ...')

    else:
        print(f'YEAAAH!!!! You guessed it in {number_of_guesses} guesses.')
        break
