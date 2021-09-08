import pandas as pd

df1 = pd.DataFrame({'this_key': ['A', 'B', 'C', 'D'],
                	'this_value': [1, 2, 3, 4]})

df2 = pd.DataFrame({'that_key': ['C', 'D', 'E', 'F'],
                	'that_value': [9, 8, 7, 6]})

# Keys are different names so we have to specify "left_on" and "right_on"

df3 = pd.merge(df1,df2,left_on='this_key',right_on='that_key',how='left')

print('Left DataFrame:\n')
print(df1)

print('\nRight DataFrame:\n')
print(df2)

print('\nLeft Join:\n')
print(df3)
