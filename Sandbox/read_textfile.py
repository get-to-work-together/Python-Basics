import re
import sys
import os.path

filename_in = 'attendentsX.csv'
filename_out = 'attendents_only.csv'

if not os.path.exists(filename_in):
    print('File does not exist')
    sys.exit()

try:
    with open(filename_in, encoding = 'utf8') as f_in:  # utf8 or cp1252
        with open(filename_out, mode = 'w') as f_out:
            for linenr, line in enumerate(f_in, start=1):
                line = line.strip()
                if re.search(r'[\w\.]+@\w+\.\w{2,3}', line):
                    fields = line.split(';')
                    print(fields)
                    f_out.write(f'{linenr}: {fields[-1]}\n')

except FileNotFoundError:
    print('That file does not exist')

except Exception as ex:
    print(f'Error: {ex}')
    print(sys.exc_info()[2].tb_lineno)