
filename_in = 'data.txtX'
filename_out = 'out.txt'

try:
    with open(filename_in) as f_in:
        with open(filename_out, mode = 'a') as f_out:
            for line in f_in:
                line = line.rstrip('\n')
                if '@' in line:
                    print(line, file = f_out)

except FileNotFoundError:
    print('File does not exist')
