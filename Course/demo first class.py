

def add(x1, x2):
    return x1 + x2


def multiply(x1, x2):
    return x1 * x2


def do_something(x1, x2, f):
    return f(x1, x2)


functions = {
    'f1': lambda *args: sum(args),
    'f2': multiply,
    'f3': lambda x1, x2: abs(x1 - x2),
    'f4': lambda x1, x2: abs(x1 ** 2 - x2 ** 2) ** 0.5
}

f = 'f4'
print( do_something(5, 10, functions[f]) )
