
def drange(start, stop, step=1.0, endpoint=False):
    eol = False
    number = start
    while not eol:
        yield number
        number += step
        if endpoint:
            if number > stop:
                eol = True
        else:
            if number >= stop:
                eol = True


