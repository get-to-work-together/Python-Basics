def drange(start, stop, step=1, include_endpoint=False):
    numbers = []
    number = start
    while True:
        numbers.append(number)
        number = round(number + step, 12)
        if include_endpoint:
            if number > stop:
                break
        else:
            if number >= stop:
                break
    return numbers



def grange(start, stop, step=1, include_endpoint=False):
    number = start
    while True:
        yield number
        number = round(number + step, 12)
        if include_endpoint:
            if number > stop:
                break
        else:
            if number >= stop:
                break


# -------------------------------------------------------

print(drange(1, 10))
print(drange(1, 10, include_endpoint=True))

print(drange(1, 5, 0.5))
print(drange(1, 5, 0.5, include_endpoint=True))


print(drange(1, 2, 0.1, include_endpoint=True))

print(list(grange(1, 2, 0.1, include_endpoint=True)))
