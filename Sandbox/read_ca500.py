filename = 'ca-500.csv'

with open(filename) as f:
    line = f.readline()
    line = line.rstrip('\n')
    headers = line.split(';')
    for line in f:
        line = line.rstrip('\n')
        columns = line.split(';')
        d = dict(zip(headers, columns))
        if d['city'] == 'Montreal':
            print(d['first_name'], d['last_name'], d['city'])
