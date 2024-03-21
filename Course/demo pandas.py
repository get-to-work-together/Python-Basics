import pandas as pd

print(pd.__version__)

pd.set_option('display.max_rows', 1000)

filename = 'ca-500.csv'
filename = r'/Users/peter/Computrain/_InCompany/ASML/Python Basics/Sandbox/ca-500.csv'

df = pd.read_csv(filename, sep=';')

df['full_name'] = df['first_name'] + ' ' + df['last_name']


print(list(df.columns))


print(df.info())

df2 = df[   ['first_name','last_name','full_name','city']    ]

df3 = df2.query('city == ["Montreal", "Toronto"]')

print( df2[df2['city'].isin(["Montreal", "Toronto"])] )


df.query('z > 0.5')
df[ df['z'] > 0.5 ]
df[ df.iloc[:, 2] > 0.5 ]

# print(df3)
#
# print( df3['city'].value_counts() )