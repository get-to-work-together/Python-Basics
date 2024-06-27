import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 1000)

filename = 'ca-500.csv'

df = pd.read_csv(filename, sep=';')

print(df.info())

print(df.query('city=="Vancouver"')[['first_name', 'last_name','city']].sort_values('first_name').head(100))

print(df.groupby('city').size().sort_values())

grouped = df.groupby('province').size()

grouped.plot(kind='barh')
plt.show()

