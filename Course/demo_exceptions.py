
class InvalidArgumentError(Exception):
    pass


def calculate_area(width, height):
    if width < 0:
        raise InvalidArgumentError('Invalid argument: negative width')
    if height < 0:
        raise InvalidArgumentError('Invalid argument: negative height')
    return width * height


#------------------


while True:
    w = float(input('Width: '))
    h = float(input('Height: '))

    # EAFP                         
    try:        
        print(calculate_area(w, h))
        break

    except InvalidArgumentError as ex:
        print(f'An error occored: {ex}')
        print('Please try again')

    # LBYL
##    if w >= 0 and h >= 0:
##        print(calculate_area(w, h))
##        break
##
##    else:
##        print(f'An error occored')
##        print('Please try again')
