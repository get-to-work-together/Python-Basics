import pandas as pd

filename = 'data.csv'

df = pd.read_csv(filename, sep=';', decimal=',', date_format='%d-%m-%Y')

print(df)