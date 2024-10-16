def say_something(name, repeat = 1):
    s = ''
    for _ in range(repeat):
        s += f'Hi {name}\n'
    return s, s.lower(), s.upper()


original, lower, upper = say_something(repeat = 3, name = 'Peter')

print(lower)
