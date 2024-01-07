
def calculate_cube(number):
    """Calculate the cube of a number

    >>> calculate_cube(10)
    1000

    >>> calculate_cube(5)
    125
    """
    return number * number * number



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
