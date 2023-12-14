import os

filename = 'data.csv'

try:
    if os.path.exists(filename):
        with open(filename, encoding = 'utf-8') as f:

            header = f.readline().strip()
            headers = header.split(';')

            for line in f:
                line = line.strip()
                values = line.split(';')
                d = dict(zip(headers, values))
                if d['city'] == 'Eindhoven':
                    print(d)
                    denominator = int(d['number'])
                    if denominator != 0:
                        print('quotient is', 100/denominator)
                    else:
                        print('Cannot devide by 0')

    else:
        print(f'File {filename} doesnot exist.')

except FileNotFoundError:
    print(f'Cannot find file {filename}')

except ValueError:
    print('Trying to convert a non number to a number')

except ZeroDivisionError:
    print('Even in 2023 you can not divide by 0')