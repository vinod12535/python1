import pandas as np
ls=['','?','Na','N/A','n/a','-']
df=pd.read_csv('autompg.csc',na_values=ls)

print("to print 10 record of dataset",df.head())
print("to statistical summary",df.describe())
print("to print information about datatype and null entries",df.info())

print("to check missing values in dataset",isnull().sum())
df.fillna(df['horsepower'].mean(),inplace=True)
print("verify missing values are required in dataset",df.isnull(),sum())

print("selecting a subset of data",df[['horsepower','cylinder']])

#univariate
import matplotilb.pyplot as plt
import seaborn as sns
plt.hist(df['horsepower'])
plt.show()
plt.boxplot(df['horsepower'])
plt.show()

#bivariate
sns.heatmap(df[['horsepower','cylinders','weight']].corr(),annot=True)
plt.show()

Q1,Q3=df['horsepower'].quentile([0,25,0,75])
IQR=Q3-Q1
lower


