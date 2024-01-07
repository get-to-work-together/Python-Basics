import re

filename = 'data.csv'

with open(filename) as f:
    headers = f.readline().strip().split(',')
    for line in f:
        line = line.strip()

        m = re.search(r'^(\w+) (\w+),(\w+),(.+)$', line)
        first_name, last_name, residence, email = m.groups()

        print(first_name, last_name, residence, email)