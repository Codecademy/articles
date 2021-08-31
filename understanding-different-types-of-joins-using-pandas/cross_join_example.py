import pandas as pd

df1 = pd.DataFrame({ 'quarter': ['Q1', 'Q2', 'Q3', 'Q4']})

df2 = pd.DataFrame({ 'month_of_quarter': [1,2,3]})

# When using a cross join, no keys are specified
df3 = df1.merge(df2, how='cross')

print('Left Dataframe:\n')
print(df1)

print('\nRight Dataframe:\n')
print(df2)

print('\nCross Join:\n')
print(df3)
