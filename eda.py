import pandas as pd #pandas library
import seaborn as sns #seaborn charting built in matplotlib
from matplotlib import pyplot as plt #use matplotlib for tweaks
import numpy as np #for zero conversion
%matplotlib inline 
#keep plots in notebook
from sklearn import preprocessing

df = pd.read_csv("Book1.csv") # read the data from csv other methods for other formats
# can add to read () encoding = 'utf-16' or ISO8893-1 or latin1 to avoid read errors
df.shape # attribute returns a colums, rows, total
df.head() # shows the first 5 rows and corresponding columns
df.tail() # last 5 rows. Can place numbers in the () to get more or less rows
df.describe() # gives the following information: count, mean, std, min, 25%, 50%, 75%, max 
df.info() # columns, non-null counts, Dtypes
df.columns # shows the same without using for loop

#Dropping na values
#Find columns with na values
df.isna().sum()
 
#Find percentage of na values in each column
(((df.isna().sum()) / (df.count() + df.isna().sum()) ) * 100).sort_values(ascending = False)

#To eliminate 0 values make them na values and then remove them
df_no_zero = df
df_no_zero = df_no_zero.replace(0, np.nan).dropna(axis=0, how='any', subset=['...']) #subset of columns if needed

df_numeric = df.select_dtypes(include = ['float64', 'int64']) # Once you know what datatypes you are seeking, create a df with only numeric values

#In order to correlate values need to be numeric. Can convert non numeric with pd.get_dummies() or with sklearn
df1 = pd.get_dummeies(df)

#sklearn method
le = preprocessing.LabelEncoder()
df2 =df
df2['...'] = le.fit_transform(df['...'])

#density plots on same graph
sns.distplot(df1[df1.... == 1]["..."])
sns.distplot(df1[df1.... == 0]["..."]).set(title='Charges Density Plot')

#Other plots box plot, scatter, lmplot, catplot
sns.catplot(x='sex', y='charges', hue='smoker', kind='box', data=df).set(title='Charges based on Smoking and Sex')
sns.catplot(x='sex', y='charges', hue='smoker', data=df).set(title='Charges based on Smoking and Sex')
sns.lmplot(x="age", y="charges", hue="smoker", data=df).set(title='Charges based on Age and Sex')
sns.catplot(x="smoker", kind='count', hue='sex', data=df).set(title='Smoker Counts Differentiated by Gender')

df_numeric.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8, annot=True) #Plot all variables in a histogram format
df1.corr(numeric_only=True) #use this if you do not want to waste time with non numeric values

df_num_corr = df_numeric.corr()['...'] #use numeric df and correlate with pandas.corr method to one variable column
golden = df_num_corr[df_num_corr > 0.5 or df_num_corr < 0.5].sort_values(ascending=False) # makes a list of correlated values > 0.5
print(f"There is {len(golden)} strongly correlated values with ... :\n{golden}") # prints analysis

#Heat map for graphical analysis of correlation
plt.figure(figsize=(9, 7))
sns.heatmap(df.corr(), vmin=-1, vmax=1, cmap='Spectral').set_title("Correlation Plot")

for i in range(0, len(df_numeric.columns), 5): # make colums of 5 and plot the correlation data 
    sns.pairplot(data=df_numeric, x_vars=df_numeric.columns[i:i+5], y_vars=['...'])

