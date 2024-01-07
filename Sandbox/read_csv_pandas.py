import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 1000)

filename = 'ca-500.csv'

df = pd.read_csv(filename, sep=';')

df_montreal = df[['first_name', 'last_name', 'city', 'province', 'email']]

df_montreal = df.query('city=="Montreal"')

print(df_montreal)

df['province'].value_counts().plot(kind='bar')
plt.show()
