import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("mpg")

sns.set()

# Example 1: Histogram
jp = df.loc[df.loc[:,'origin'] == 'japan', ['horsepower']]
eu = df.loc[df.loc[:,'origin'] == 'europe', ['horsepower']]
 
plt.hist(x=jp, alpha=0.5, label='Japan')
plt.hist(x=eu, alpha=0.5, label='Europe')

plt.legend()
plt.xlabel('Horsepower')

plt.show()

# Example 2: KDE
dfjp = df.loc[df.loc[:,'origin'] == 'japan']
dfeu = df.loc[df.loc[:,'origin'] == 'europe']
 
sns.kdeplot(data=dfjp['mpg'], fill=True, label='Japan')
sns.kdeplot(data=dfeu['mpg'], fill=True, label='Europe')

plt.legend()
plt.xlabel('MPG')

plt.show()

# Example 3: Linear Regression
sns.lmplot(data=df, x='acceleration', y='weight')
plt.show()

# Example 4: Violin
df.loc[df.loc[:,'origin'].isin(['europe','japan']),'manufacture'] = 'foreign'
df.loc[df.loc[:,'origin'].isin(['usa']),'manufacture'] = 'domestic'

sns.violinplot(data=df, x='cylinders', y='mpg', hue='manufacture', split=True)
plt.show()

# Example 5.1: Joint plots - KDE
sns.jointplot(x='displacement',y='horsepower',data=df, kind='kde')
plt.show()

# Example 5.2: Joint plots - Hex
sns.jointplot(x='displacement',y='horsepower',data=df, kind = 'hex')
plt.show()
 
# Example 5.3: Joint plots - Scatter
sns.jointplot(x='displacement',y='horsepower',data=df, kind = 'scatter', hue='cylinders', palette='bright')
plt.show()
