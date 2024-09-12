filename = 'dir.txt'

try:
    total_size = 0
    with open(filename) as f:
        first_line = f.readline()
        for line in f:
            line = line.rstrip('\n')
            columns = line.split(maxsplit=9)
            print(columns)
            name = columns[-1]
            if name.endswith('.py'):
                size = int(columns[4])
                total_size += size

except FileNotFoundError:
    print('File does not exist')
    exit(-1)

except ValueError as ex:
    print('Wrong value', ex)
    exit(-1)

except Exception as ex:
    print('Something else went wrong', ex)
    exit(-1)



print(f'The total size of all .py files is {total_size} bytes')