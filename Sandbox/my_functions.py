def print_goodmorning(name = 'stranger'):
    print(f'Goodmorning {name}')
    print('How are you today?')
    print('Have a great day!')


def addsub(x1, x2):
    """This function does an addition and a subtraction in one go"""
    total = x1 + x2
    difference = x1 - x2
    return total, difference

#-------------------------------------------

if __name__ == '__main__':
    
    print_goodmorning('Peter')
    print_goodmorning('Joost')
    print_goodmorning()

    print(addsub(4, 5))

