import re
import os

filename = 'ca-500x.csv'
results_filename = 'results.csv'

try:

    with open(filename, 'r') as f:
        with open(results_filename, 'a') as f_out:

            headers = f.readline().strip().split(';')

            for linenr, line in enumerate(f, start = 1):
                values = line.strip().split(';')

                d = dict(zip(headers, values))

                if d['city'] in ('Montreal', 'Toronto'):
                    print(f'{linenr:3}: {d["first_name"]:20} {d["last_name"]:20} {d["email"]:40} {d["city"]:20}')

                    print(linenr, d["first_name"], d["last_name"], d["email"], d["city"], sep = ',', file = f_out)

except FileNotFoundError:
    print('File does not exist')

except:
    print('Error')