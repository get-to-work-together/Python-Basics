filename1 = 'ca-500.csv'
filename2 = 'ca-500-filtered.tsv'

with open(filename1, encoding='utf8') as f1:
    with open(filename2, 'w') as f2:

        data = f1.readline().rstrip('\n')
        header = data.split(';')

        for line in f1:

            line = line.rstrip('\n')
            row = line.split(';')

            d = dict(zip(header, row))

            if d['city'] in ('Montreal', 'Toronto'):

                print(d['first_name'],
                      d['last_name'],
                      d['city'])

                f2.write('%s\t%s\t%s\n' % (d['first_name'],
                                           d['last_name'],
                                           d['city']))


