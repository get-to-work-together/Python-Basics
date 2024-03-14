
class InvalidArgumentError(Exception):
    pass


def calculate_area(width, height):
    if width < 0 or height < 0:
        raise InvalidArgumentError('Invalid argument')

    return width * height


while True:
    w = float(input('Give width: '))
    h = float(input('Give height: '))

    try:
        area = calculate_area(w, h)
        print(area)

    except Exception as ex:
        print(ex)
        continue