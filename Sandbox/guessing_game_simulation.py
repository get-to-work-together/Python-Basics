import random
import sys
import math

LOW = 1
HIGH = 100


class GuessingGame:

    def __init__(self, low=LOW, high=HIGH, random_state=None):
        self._low = low
        self._high = high
        if random_state:
            random.seed(random_state)
        self._secret_number = random.randint(low, high)
        self._number_of_guesses = 0

    def guess(self, guess):
        self._number_of_guesses += 1
        if guess > self._secret_number:
            return 1  # is larger
        elif guess < self._secret_number:
            return -1  # is smaller
        elif guess == self._secret_number:
            return 0  # correct

    @property
    def secret_number(self):
        return self._secret_number

    @property
    def number_of_guesses(self):
        return self._number_of_guesses


class PlayGuessingGame:

    def __init__(self, low=LOW, high=HIGH):
        self._low = low
        self._high = high
        self._game = GuessingGame(low, high)

    def guess_input(self):
        while True:
            try:
                guess = int(input('What is your next guess? '))
                if self.LOW <= guess <= self.HIGH:
                    return guess
                else:
                    print(f'That is not a number between {self._low} and {self._high}.')
            except:
                print('That is not a valid number.')

    def play(self):

        print('Guess a number between %d and %d' % (self._low, self._high))
        while True:
            myGuess = self.guess_input()

            result = self._game.guess(myGuess)

            if result == 1:
                print('lower ...')
            elif result == -1:
                print('higher ...')
            elif result == 0:
                print('YEAAAH! You guessed it in {} guesses'.format(self._game.number_of_guesses))
                break


class GuessingGameAutoPlayer:

    def __init__(self, low=LOW, high=HIGH, verbose=True, strategy=None, random_state=None):
        self._low = low
        self._high = high
        self._game = GuessingGame(low, high, random_state=random_state)
        self._verbose = verbose
        if strategy is None:
            self._strategy = GuessingGameAutoPlayer.guess_middle
        else:
            self._strategy = strategy

    def guess_random_between(self):
        return random.randint(self._low, self._high)

    def guess_first_64_then_middle(self, first_guess=None):
        return self.guess_middle(first_guess=64)

    def guess_middle(self, first_guess=None):
        if first_guess and self._game.number_of_guesses == 0:
            return first_guess
        else:
            return (self._low + self._high) // 2

    def guess_power_of_two(self):
        assert self._low <= self._high, f'Error: no numbers between {self._low} and {self._high}'

        d = self._high - self._low + 1
        log_d = math.log2(d / 2)

        if self._high == self._low:
            return self._low
        elif d == 1:
            d2 = 2
        elif log_d == int(log_d):
            d2 = 2 ** int(log_d)
        else:
            d2 = 2 ** int(round(log_d))
        return self._low + d2 - 1

    def guess(self):
        return self._strategy(self)

    def play(self):

        while True:
            next_guess = self.guess()
            if self._verbose:
                print(next_guess)

            result = self._game.guess(next_guess)

            if result == 1:
                self._high = next_guess - 1
            elif result == -1:
                self._low = next_guess + 1
            elif result == 0:
                if self._verbose:
                    print(
                        f'YEAAAH! The secret number was {self._game.secret_number}. You guessed it in {self._game.number_of_guesses} guesses.')
                break

            if self._high < self._low:
                if self._verbose:
                    print('You cheated! I quit!')
                sys.exit(-1)

        return self._game.number_of_guesses


# ----------------------------------------------------------

def simulation(number_of_games=100000, verbose=False, strategy=None, random_state=None):
    if random_state:
        random.seed(random_state)

    number_of_guesses_counter = dict()
    for i in range(number_of_games):
        number_of_guesses = GuessingGameAutoPlayer(verbose=verbose, strategy=strategy).play()
        number_of_guesses_counter[number_of_guesses] = number_of_guesses_counter.get(number_of_guesses, 0) + 1

    print(f'\n{strategy.__name__}')

    total_number_of_guesses = 0
    for guess, freq in sorted(number_of_guesses_counter.items()):
        total_number_of_guesses += guess * freq
        proportion = freq / number_of_games
        print(f'{guess:3} {"█" * round(proportion * 100)} {proportion * 100:.1f}%')

    print(f'Total number of guesses {total_number_of_guesses}')

    return number_of_games, total_number_of_guesses


if __name__ == '__main__':
    # PlayGuessingGame().play()

    # GuessingGameAutoPlayer(strategy = GuessingGameAutoPlayer.guess_middle).play()
    # GuessingGameAutoPlayer(strategy = GuessingGameAutoPlayer.guess_first_64_then_middle).play()
    # GuessingGameAutoPlayer(strategy = GuessingGameAutoPlayer.guess_power_of_two).play()

    random_state = random.randint(1, 100000)
    simulation(strategy = GuessingGameAutoPlayer.guess_random_between, random_state = random_state)
    # simulation(strategy=GuessingGameAutoPlayer.guess_middle, random_state=random_state)
    # simulation(strategy = GuessingGameAutoPlayer.guess_first_64_then_middle, random_state = random_state)
    # simulation(strategy = GuessingGameAutoPlayer.guess_power_of_two, random_state = random_state)
