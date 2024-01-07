import re
import csv

filename = 'ca-500.csv'

with open(filename, 'r') as f:
    reader = csv.DictReader(f, delimiter=';')

    for d in reader:

        if d['city'] in ('Montreal', ):

            print('%-15s %-15s %-35s %-25s' %
                  (d['first_name'], d['last_name'], d['email'], d['city']))

