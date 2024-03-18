#!/usr/bin/python

import os
import pandas as pd

filename = 'ca-500.csv'

df = pd.read_csv(filename, sep = ';')

df = df.query('city=="Montreal"')

print(df[['first_name', 'last_name', 'city']])