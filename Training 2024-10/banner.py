
def banner(text, c='*'):
    if not c:
        c = '*'
    n = len(text)
    top_and_bottom_line = c * (n + 6)
    print(top_and_bottom_line)
    print(f'{c}  {text}  {c}')
    print(top_and_bottom_line)


# ----------------------------------------------------------

if __name__ == '__main__':

    name = input('What is your name? : ')
    c = input('Which character do you want to use? : ')

    banner(name, c)
