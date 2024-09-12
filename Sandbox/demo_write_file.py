filename = 't.txt'

with open(filename, 'w') as f:

    f.write('line1\n')
    f.write('line2\n')
    f.write('line3\n')

    print('line4', file=f)
    print('line5', file=f)