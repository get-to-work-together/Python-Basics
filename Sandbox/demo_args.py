

def f(*args, **kwargs):
    print('args:', args)
    print('kwargs:', kwargs)

# ---------

f(1, 2, 3, 4, 5)
f(a=1, b=2, c=3)
f(1, 2, a='a', b='b')

