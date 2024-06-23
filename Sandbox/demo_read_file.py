import os
import re

print('Current working directory', os.getcwd())

filename_in = 'data.txt'
filename_out = 'data_out.txt'

try:
    with open(filename_in, mode='r') as f_in:
        with open(filename_out, mode='w') as f_out:

            for i, line in enumerate(f_in, start = 1):
                line = line.strip()
                if re.search(r'\w+@\w+\.\w{2,3}', line):
                    print(i, line)
                    print(i, line, file = f_out)

except FileNotFoundError:
    print(f'Cannot find file {filename_in}')