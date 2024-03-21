filename = 'data.txt'
# or
# filename = '/Users/peter/Computrain/_InCompany/ASML/Python Basics/Course/data.txt'
# filename = r'C:\Users\peter\Computrain\_InCompany\ASML\Python Basics\Course\data.txt'

with open(filename) as f:
    with open('output.txt', 'w') as fout:

        headers = f.readline().strip().split(',')
        print(headers)

        for line in f.readlines():
            values = line.strip().split(',')
            d = dict(zip(headers, values))
            temp = int(d['t'])
            if 70 < temp < 90:
                print(f'nr {d["nr"]} ==> {temp}')
                print(f'nr {d["nr"]} ==> {temp}', file = fout)

print('Done')
