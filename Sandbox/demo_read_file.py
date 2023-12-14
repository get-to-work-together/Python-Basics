import os
print('Current working directory', os.getcwd())

filename = 'data.txt'
# filename = '/Users/peter/Computrain/_InCompany/ASML/Python Basics/Sandbox/data.txt'


with open(filename, mode='r') as f:

    for line in f:
        line = line.strip()
        if 'and' in line:
            print(line)


with open('demo.txt', mode = 'w') as f:

    f.write('This is my first line\n')

    print('And this is the second', file = f)
