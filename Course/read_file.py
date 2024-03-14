filename = 'data.txt'
filename = '/Users/peter/Computrain/_InCompany/ASML/Python Basics/Course/data.txt'
# filename = r'C:\Users\peter\Computrain\_InCompany\ASML\Python Basics\Course\data.txt'

filename_out = '.\python basics\output.txt'

try:
    with open(filename) as f:
        with open(filename_out, mode = 'a') as f_out:

            header = f.readline()
            headers = [item.strip() for item in header.split(',')]

            for line in f:
                columns = [item.strip() for item in line.split(',')]

                d = dict(zip(headers, columns))
                if d['city'] in ('Eindhoven','Veldhoven'):
                    print(d['first_name'], d['last_name'], d['city'])
                    # print(d['first_name'], d['last_name'], d['city'], file = f_out)
                    age = int(d['age'])
                    f_out.write(';'.join([d['first_name'], d['last_name'], d['city']]) + '\n')

except FileNotFoundError:
    print(f'Cannot find file {filename}.')

except ValueError:
    print('Invalid number')

else:
    print('In else block')

finally:
    print('In finally block')

print('Normal block')