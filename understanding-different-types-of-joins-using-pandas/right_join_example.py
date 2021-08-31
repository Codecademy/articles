import pandas as pd

df1 = pd.DataFrame({'this_key': ['A', 'B', 'C', 'D'],
                	'value': [1, 2, 3, 4]})

df2 = pd.DataFrame({'that_key': ['C', 'D', 'E', 'F'],
                	'value': [9, 8, 7, 6]})

# .merge() can be used as a method of a dataframe object.
# When used this way, the dataframe using the method is the "left" dataframe.

# Without using "suffixes", the default ones of "_x" and "_y" are used.

df3 = df1.merge(df2,left_on='this_key',right_on='that_key',how='right')

print('Left Dataframe:\n')
print(df1)
print('\nRight Dataframe:\n')
print(df2)
print('\nRight Join:\n')
print(df3)
