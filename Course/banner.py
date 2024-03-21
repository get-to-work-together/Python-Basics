
def print_banner(name, c = '*'):
    stars = c * (len(name) + 6)
    print(stars)
    print(c + '  ' + name + '  ' + c)
    print(stars)


if __name__ == '__main__':

    print_banner('Peter', c = '$')
