filename = 'ca-500.csv'

filename_windows = 'C:\Users\Peter\Documents\data.txt'

filename_windows = 'C:\\Users\\Peter\\Documents\\data.txt'
filename_windows = r'C:\Users\Peter\Documents\data.txt'
filename_windows = 'C:/Users/Peter/Documents/data.txt'


with open(filename) as f:
    line = f.readline()
    line = line.rstrip('\n')
    headers = line.split(';')
    for linenr, line in enumerate(f, start=2):
        line = line.rstrip('\n')
        columns = line.split(';')
        d = dict(zip(headers, columns))
        if d['city'] == 'Montreal':
            print(f'{linenr:3}:', d['first_name'], d['last_name'], d['city'])
