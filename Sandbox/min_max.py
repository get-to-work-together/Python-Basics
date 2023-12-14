
def min_max(*values):
    minimum = values[0]
    maximum = values[0]
    for value in values[1:]:
        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value
    return minimum, maximum

#--------------------------------------------------

if __name__ == '__main__':

    values = [6,2,8,3,5,7,1,4]

    print(min_max(*values))
