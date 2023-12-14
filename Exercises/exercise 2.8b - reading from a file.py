filename = 'demo_open.txt'

with open(filename) as f:

    headers = f.readline().rstrip('\n').split(',')

    for line in f:
        columns = line.rstrip('\n').split(',')

        d = dict(zip(headers, columns))

        if d['ID'] == '1003':
            print(d)
