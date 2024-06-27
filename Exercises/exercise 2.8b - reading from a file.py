import sys

filename = 'demo_open.txt'

with open(filename) as f:
    with open('output.txt', 'w') as f_out:

        headers = f.readline().rstrip('\n').split(',')

        for linenr, line in enumerate(f, start=2):
            line = line.rstrip('\n')
            columns = line.split(',')

            d = dict(zip(headers, columns))

            if d['ID'] == '1003':
                print(f'{linenr:3}: {line}')

                print(f'{linenr:3}: {line}', file=f_out)
                f_out.write(f'{linenr:3}: {line}\n')


