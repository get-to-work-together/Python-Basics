import random

def minmax(nrs):
    minimum = nrs[0]
    maximum = nrs[0]
    for number in nrs[1:]:
        if number > maximum:
            maximum = number
        if number < minimum:
            minimum = number
    return minimum, maximum
        

# ------------------------------------------------

if __name__ == '__main__':

    numbers = [random.randint(1,100) for _ in range(20)]

    lowest, highest = minmax(numbers)

    print('lowest number', lowest)
    print('highest number', highest)
