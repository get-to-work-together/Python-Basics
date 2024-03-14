

def show_arguments(*args, offset=None, factor=None, **kwargs):
    print(args)
    print(offset)
    print(factor)
    print(kwargs)


show_arguments('Peter', 10, 'Lhee', 98798, 8947, c = '*')

numbers = [2,3,4,5]
settings = {'offset': 2.5, 'factor': 10, 'valid': True}
show_arguments(*numbers, **settings)