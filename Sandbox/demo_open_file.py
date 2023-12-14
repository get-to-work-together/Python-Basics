

filename = 'email_addresses.txtx'
# filename = 'email_addresses.txt'   # windows
# filename = r'email_addresses.txt'   # windows

with open(filename) as f:
    for line in f:
        line = line.rstrip('\n')
        if 'asml' in line:
        # if line.endswith('asml.com'):
            print(line)