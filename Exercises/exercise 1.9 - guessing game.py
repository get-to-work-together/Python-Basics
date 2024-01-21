import random

lower = 1
upper = 100

magic_number = random.randint(lower, upper)

print(f'Guess a number between {lower} and {upper}.')
number_of_guesses = 0

while True:

    guess = int(input(f'What is your guess? '))

    number_of_guesses += 1

    if guess > magic_number:
        print('lower ...')

    elif guess < magic_number:
        print('higher ...')

    else:
        print(f'YEAAAH!!!! You guessed it in {number_of_guesses} guesses.')
        break






##while True:
##
##    first_or_next = 'first' if number_of_guesses == 0 else 'next'
##    user_input = input(f'What is your {first_or_next} guess? ')
##
##    if user_input.isnumeric():
##        guess = int(user_input)
##    else:
##        print('That is not a number')
##        continue
##
##    number_of_guesses += 1
##
##    if guess > magic_number:
##        print('lower ...')
##
##    elif guess < magic_number:
##        print('higher ...')
##
##    else:
##        print(f'YEAAAH!!!! You guessed it in {number_of_guesses} guesses.')
##        break
