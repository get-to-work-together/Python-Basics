import os

filename = 'data.csv'
out_filename = 'data.tsv'

try:
    with open(filename, mode = 'r') as f:
        with open(out_filename, mode = 'w') as f_out:

            first_line = f.readline().strip()
            headers = first_line.split(';')

            for line in f:
                line = line.strip()
                values = line.split(';')

                d = dict(zip(headers, values))

                if d['department'] == 'a':

                    print(f"{d['id']:10} {d['B']:10} {d['department']}")

                    f_out.write(f"{d['id']:10}\t{d['B']:10}\t{d['department']}\n")

except FileNotFoundError:
    print(f'Cannot find file {filename}')
