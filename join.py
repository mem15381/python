import pandas as pd
import jdatetime 
df1 = pd.read_csv('dollar.csv')
df2 = pd.read_csv('shakhes.csv')
df3 = df1.join(df2, lsuffix='jDate', rsuffix='date')
df3.to_csv('join.csv')
print(df3.head())
