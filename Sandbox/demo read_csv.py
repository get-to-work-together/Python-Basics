import pandas as pd
import os

print(os.getcwd())

df = pd.read_csv('ca-500.csv', sep=';', decimal=',')


print(list(df.columns))

print(df.shape)

df_selection = df.loc[df['city']=='Montreal' ,['first_name','last_name','city']]

print(df_selection)