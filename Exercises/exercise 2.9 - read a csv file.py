filename_in = '../Sandbox/ca-500.csvX'
filename_out = '../Sandbox/ca-out.txt'

try:
    with open(filename_in) as f_in:
        with open(filename_out, mode = 'w') as f_out:
            headers = f_in.readline().strip().split(';')

            for line in f_in:
                line = line.strip()
                values = line.split(';')

                d = dict(zip(headers, values))

                if d['city'] == 'Montreal':
                    print(f"{d['first_name']:16} {d['last_name']:16} {d['city']:16} {d['email']}")

                    print(f"{d['first_name']:16} {d['last_name']:16} {d['city']:16} {d['email']}", file = f_out)

except FileNotFoundError:
    print(f'Cannot find the file: {filename_in}')