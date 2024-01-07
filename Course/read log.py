import re

filename = 'example.log'

with open(filename) as f:
    for line in f:
        line = line.strip()
        m = re.match(r'^(.+)\,(.+\..+)-(.+)$', line)
        if m:
            ts, id, message = m.groups()
            print(ts, '=>', message)