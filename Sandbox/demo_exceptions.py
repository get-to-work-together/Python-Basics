
class MyInvalidArgumentError(Exception):
    pass


def calculate_area(width, height):

    if width < 0 or height < 0:
        raise MyInvalidArgumentError('Negative argument')

    # or

    assert width >= 0 and height >= 0, 'Negative argument'

    return width * height

# ---------------------------

try:
    # open database
    area = calculate_area(10, -2)
    print(area)

except AssertionError as err:
    print(err)

except MyInvalidArgumentError:
    print('My bussiness rules have been violated!')

else:
    print('Everything went well!')

finally:
    # close database
    print('Always executed!')
