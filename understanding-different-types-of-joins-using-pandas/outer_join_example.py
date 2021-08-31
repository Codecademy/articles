import pandas as pd

df1 = pd.DataFrame({'this_key': ['A', 'B', 'C', 'D'],
                	'value': [1, 2, 3, 4]})

df2 = pd.DataFrame({'that_key': ['C', 'D', 'E', 'F'],
                	'value': [9, 8, 7, 6]})

# Specifying "indicator" will provide a column stating the source of the data for each row
df3 = df1.merge(df2,left_on='this_key',right_on='that_key',how='outer',indicator='source')

print('Left Dataframe:\n')
print(df1)
print('\nRight Dataframe:\n')
print(df2)
print('\nOuter Join:\n')
print(df3)
