import sys

filename = 'demo_open.txtX'

try:
    with open(filename) as f:

        headers = f.readline().rstrip('\n').split(',')

        for linenr, line in enumerate(f, start=2):
            line = line.rstrip('\n')
            columns = line.split(',')

            d = dict(zip(headers, columns))

            if d['ID'] == '1003':
                print(f'{linenr:3}:{line}')

except FileNotFoundError:
    print(f'Can not find file: {filename}')
    sys.exit(-1)
    
