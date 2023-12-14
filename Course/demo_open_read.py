filename = 'email.txt'

try:
    with open(filename) as f:

        for linenr, line in enumerate(f, 1):
            line = line.strip()

            if linenr == 5:
                print(linenr, line)
            

##            if '@' in line:
##                name, domain = line.split('@')
##                first_name, last_name = name.split('.', maxsplit = 1)
##                
##                if domain == 'asml.com':
##                    print(f'{first_name.title():16} {last_name.replace(".", " ").title():16} => {name}@{domain}')


except FileNotFoundError:
    print(f'Cannot find file {filename}')
