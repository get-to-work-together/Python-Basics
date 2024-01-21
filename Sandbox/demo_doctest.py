import doctest


def square(x):
    """Calculate the square of x.

    >>> square(4)
    16

    >>> square(-9)
    81

    >>> round(square(1.3), 12)
    1.69
    """
    
    return x ** 2


if __name__ == "__main__":
    doctest.testmod(verbose=True)
