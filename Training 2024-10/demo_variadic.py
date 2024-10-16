
def my_function(n, *args, red=1, green=2, orange=3, **kwargs):
    print(n)
    print(args)
    print(red)
    print(green)
    print(orange)
    print(kwargs)
    if not kwargs:
        print('No extra keyword arguments')
    second_function(*args, **kwargs)


def second_function(*args, **kwargs):
    print(args)
    print(kwargs)


my_function( 23, 'abc', 'xyz', orange=5)
