import re
import os

filename = 'ca-500.csv'

try:

    with open(filename, 'r') as f:

        headers = f.readline().strip().split(';')

        for linenr, line in enumerate(f, start = 2):
            values = line.strip().split(';')

            d = dict(zip(headers, values))

            name, domain = d['email'].split('@')
            d['name'] = name
            d['domain'] = domain

            if d['city'] in ('Montreal', ):
                print(f'{linenr:3}: {d["first_name"]:20} {d["last_name"]:20} {d["email"]:40} {d["city"]:20} {d["domain"]}')

except FileNotFoundError:
    print('File does not exist')

except:
    print('Error')