
class InvalidArgumentException(Exception):
    pass


def calculate_area(width, height):
    if width < 0 or height < 0:
        raise InvalidArgumentException('Invalid argument')
    return width * height


try:
    area = calculate_area(10, -2)
    print(area)

except InvalidArgumentException as err:
    print(type(err), err)
