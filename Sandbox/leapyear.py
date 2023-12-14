from __future__ import print_function

def is_leapyear(y):
    """This is a function to determine if a year is a leapyear or not.

    Argument: year
    Return value: True or False"""
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


# ----------------------------------------------------------

if __name__ == '__main__':

    year = int(input('Give a year: '))

    if is_leapyear(year):
        print('%d is a leap year' % year)
    else:
        print('%d is not a leap year' % year)
