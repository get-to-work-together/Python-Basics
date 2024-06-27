import logging
import os

logging.basicConfig(filename = 'error.log', # or to a file 'example.log',
                    level = logging.WARNING,  # Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
                    format = '%(asctime)s.%(msecs)03d - %(name)s - %(levelname)s - %(message)s',
                    datefmt = '%Y-%m-%dT%H:%M:%S')

filename = 'data2.txtXXX'

if not os.path.exists(filename):
    print(f'{filename} does not exist.')
    exit()

try:
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            if 'error' in line:
                print(line)

except FileNotFoundError:
    logging.error(f'Can not find file {filename}')

except ZeroDivisionError:
    logging.critical('Still can not divide by 0')
    exit(-1)

