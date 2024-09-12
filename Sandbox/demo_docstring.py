def cube(x):
    """Calculate the third power of x

    >>> cube(3)
    27

    >>> [cube(x) for x in range(1, 11)]
    [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
    """
    return x ** 3


class Temp(object):

    def __init__(self, name):
        self.name = name.capitalize()

    def __str__(self):
        return self.name


# import unittest
# class Tests(unittest.TestCase):
#
#     def test_simple(self):
#         actual = cube(3)
#         expected = 27
#         self.assertEqual(expected, actual)
#
#     def test_my_class(self):
#         t = Temp('peter')
#         actual = str(t)
#         expected = 'peter'
#         self.assertEqual(expected, actual)



if __name__ == '__main__':

    # import doctest
    # doctest.testmod(verbose=True)

    # unittest.main()

    t = Temp('peter')
    actual = str(t)
    expected = 'peter'
    assert expected == actual, 'Something is wrong'
