def banner(text, c = '*'):
    """Print the text as a banner"""
    n = len(text)
    print(c * (n + 6))
    print(c + '  ' + text    + '  ' + c)
    print(c * (n + 6))


if __name__ == '__main__':

    print('I am module banner')
