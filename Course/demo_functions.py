import math


def print_goodmorning(name):
    print(f'Goodmorning {name}')
    print('How are you today?')
    print('Have a great day!')


def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print('\nFlight booked from %s to %s' % (fromairport, toairport))
    print('Number of adults: %d' % numadults)
    print('Number of children: %d' % numchildren)

def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    return (weight, height, bmi)


# --------------------------------------------------------------

if __name__ == '__main__':

##    print_goodmorning('Paul')
##
##    book_flight(toairport = 'LHR',
##                fromairport = 'AMS',
##                numchildren = 3,
##                numadults = 2)

    w, h, bmi = calculate_bmi(80, 1.80)
    print(bmi)

    

