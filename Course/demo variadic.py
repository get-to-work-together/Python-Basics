
def minimum_maximum(*numbers):
    lowest = numbers[0]
    highest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number
        if number > highest:
            highest = number
    return lowest, highest

def minimum_maximum(*numbers):
    return min(numbers), max(numbers)

def minimum_maximum(*numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0], sorted_numbers[-1]



print( minimum_maximum(100, 23,4,6,8,34,56,34, 34, 65, 67, 8) )




# def print_settings(offset=0, factor=1, switch1=False, switch2=False, switch3=False):
def print_settings(*args, **kwargs):
    print('Settings:')
    for k, v in kwargs.items():
        print(k, v)

# print_settings(offset=123, factor=4.5, switch1=False, switch2=True)
# print_settings(offset=123, factor=4.5, switch1=False, switch2=True, switch3=True)


settings = {
    'offset': 0,
    'factor': 1,
    'switch1': False,
    'switch2': False,
    'switch3': False
}

print_settings(**settings)


def remove_all(item, items):
    temp = items.copy()
    while item in temp:
        temp.remove(item)
    return temp

numbers = [2,3,4,5,2,2,3,2,3,6,7]
print(numbers)
remove_all(2, numbers)
print(numbers)


numbers = remove_all(3, [2,3,4,5,2,2,3,2,3,6,7])
print(numbers)


print( list(filter(lambda item: item != 3, numbers)) )