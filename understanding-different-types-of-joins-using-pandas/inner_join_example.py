import pandas as pd

df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'],
                	'value': [1, 2, 3, 4]})

df2 = pd.DataFrame({'key': ['C', 'D', 'E', 'F'],
                	'value': [9, 8, 7, 6]})

# The "suffixes" parameter is a tuple that specifies how to distinguish 
# columns that have the same name in both DataFrames.
# The default value is ('_x','_y').

df3 = pd.merge(df1,df2,on='key',how='inner', suffixes=('_left','_right'))

print('Left DataFrame:\n')
print(df1)
print('\nRight DataFrame:\n')
print(df2)
print('\nInner Join on "key":\n')
print(df3)
