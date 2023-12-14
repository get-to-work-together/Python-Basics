import pandas as pd

filename = 'data.csv'
df = pd.read_csv(filename, sep = ';')
print(df)