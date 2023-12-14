
def print_goodmorning(name, count = 1):
    print(f'Goodmorning {name}')
    print('How are you today?')
    for _ in range(count):
        print('Have a great day!')


def book_flight(fromairport, toairport, numadults=1, numchildren=0):
    print('\nFlight booked from %s to %s' % (fromairport, toairport))
    print('Number of adults: %d' % numadults)
    print('Number of children: %d' % numchildren)


def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi > 30:
        warning = 'too heavy'
    else:
        warning = "you're OK"
    return bmi, warning



# ----------------------------------------------------

people = ['Maarten','Panos','Pim','Heemin','Eddy','Yan']

for person in people:
    print_goodmorning(person)


book_flight(toairport = 'OSL', numadults = 2, fromairport = 'AMS')


print(calculate_bmi(98, 1.80))
