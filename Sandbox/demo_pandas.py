import os
import pandas as pd

directory = '..'

filename_application = ''
filename_requisition = ''
filename_history = ''

df_application = pd.read_csv(os.path.join([directory, filename_application]))
df_requisition = pd.read_csv(os.path.join([directory, filename_requisition]))
df_history = pd.read_csv(os.path.join([directory, filename_history]))

