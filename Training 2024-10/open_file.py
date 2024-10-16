

filename = 'data.csvX'
filename_out = 'out.csv'

with open(filename_out, mode = 'w') as f_out:
    with open(filename) as f:

        headers = f.readline().rstrip('\n').split(';')

        for line in f:
            columns = line.rstrip('\n').split(';')
            d = dict(zip(headers, columns))
            if d['name'].startswith('P'):
                print(d['ID'], d['name'])
                f_out.write('|'.join(d.values())+'\n')
