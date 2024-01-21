import re

filename = 'data.txt'
##filename = '/Users/peter/Computrain/_InCompany/ASML/Python Basics/Sandbox/data.txt'
##filename = r'C:\Users\peter\Computrain\_InCompany\ASML\Python Basics\Sandbox\data.txt'
##filename = 'C:\\Users\\peter\\Computrain\\_InCompany\\ASML\\Python Basics\\Sandbox\\data.txt'

f1 = open(filename)

print('header:', f1.readline() )

f1.seek(0)

for line in f1:
    line = line.rstrip('\n')
    if re.search(r'\w+@\w+\.\w{2,3}', line):
        name, email = line.split()
        print( email )

f1.close()

