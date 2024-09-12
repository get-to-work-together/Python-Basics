

def show_arguments(*args, sep=' ', **kwargs):
    print(args)
    print(sep)
    print(kwargs)



show_arguments(1, 2, 3, sep='-', end='<<<<\n')