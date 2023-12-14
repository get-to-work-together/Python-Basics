
while True:
    try:
        number = int(input('give a number: '))

        print(number)
        print(10/number)

        break

    except ValueError:
        print('That is not a number, mom!')

    except ZeroDivisionError:
        print('Cannot divide by 0')