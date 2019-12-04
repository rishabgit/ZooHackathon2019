import pandas as pd

dataset = pd.read_csv('date_para.csv').T.to_csv('database_dates2.csv')
