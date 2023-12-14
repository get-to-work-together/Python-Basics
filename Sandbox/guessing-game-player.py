lower = 1
upper = 100

print(f'I will try to guess a number between {lower} and {upper}')

number_of_guesses = 0
while True:
    guess = (lower + upper) // 2

    response = input(f'Is your number {guess}? [higher, lower, yes] : ').lower()
    number_of_guesses += 1

    if response.startswith('h'):    # e.g. higher
        lower = guess + 1

    elif response.startswith('l'):  # e.g. lower
        upper = guess - 1

    elif response.startswith('y'):  # e.g. yes
        print(f'YEAH! Guessed it in {number_of_guesses} guesses')
        break

    else:
        print('Invalid answer!')
        number_of_guesses -= 1

    if lower > upper:
        print('You cheated! I quit.')
        break
