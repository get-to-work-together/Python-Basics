import os
import re

print('Current directory:', os.getcwd())

filename = 'ca-500x.csv'
filename_out = 'selected_lines.txt'
with open(filename, mode = 'r') as f_in:
    with open(filename_out, mode='w') as f_out:

        header = f_in.readline().strip()
        headers = header.split(';')

        for line in f_in:
            line = line.strip()
            values = line.split(';')

            d = dict(zip(headers, values))

            if d['city'].lower() in ('montreal', 'toronto'):
                print(f"{d['first_name']:20}"
                      f"{d['last_name']:20}"
                      f"{d['city']:20}"
                      f"{d['email']}")

                print(f"{d['first_name']:20}"
                      f"{d['last_name']:20}"
                      f"{d['city']:20}"
                      f"{d['email']}", file = f_out)
