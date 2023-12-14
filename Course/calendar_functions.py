
def is_leapyear(year):
    """Determine if a year is a leapyear."""
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == '__main__':
    print('Hi there!!!')