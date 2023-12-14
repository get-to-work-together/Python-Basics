
def say_hi(name, repeat = 1, uppercase = False):
    for _ in range(repeat):
        print(f'Hi {name}')
    if uppercase:
        print('How do you do?'.upper())
    else:
        print('How do you do?')
    print('Bye')


def bmi(height, weight):
    return weight / height ** 2

bmi = lambda height, weight: weight / height ** 2


if __name__ == '__main__':

    say_hi('Peter')
    say_hi('Robbert', 5, True)

    say_hi('Robbert', uppercase = True)


    print(f'Your BMI is {bmi(1.80, 96)}')

    print(height)