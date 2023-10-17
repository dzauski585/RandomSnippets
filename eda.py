import pandas as pd #pandas library
import seaborn as sns #seaborn charting built in matplotlib
from matplotlib import pyplot as plt #use matplotlib for tweaks
%matplotlib inline #keep plots in notebook

df = pd.read_csv("Book1.csv") # read the data from csv other methods for other formats
df.shape # attribute returns a colums, rows, total
df.head() # shows the first 5 rows and corresponding columns
df.tail() # last 5 rows. Can place numbers in the () to get more or less rows
df.describe() # gives the following information: count, mean, std, min, 25%, 50%, 75%, max 
df.info() # columns, non-null counts, Dtypes
df.columns # shows the same without using for loop

df_numeric = df.select_dtypes(include = ['float64', 'int64']) # Once you know what datatypes you are seeking, create a df with only numeric values
df_numeric.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8) #Plot all variables in a histogram format

df_num_corr = df_numeric.corr()['SalePrice'] #use numeric df and correlate with pandas.corr method to one variable column
golden = df_num_corr[abs(df_num_corr) > 0.5].sort_values(ascending=False) # makes a list of correlated values > 0.5
print(f"There is {len(golden)} strongly correlated values with SalePrice:\n{golden}") # prints analysis

for i in range(0, len(df_numeric.columns), 5): # make colums of 5 and plot the correlation data 
    sns.pairplot(data=df_numeric, x_vars=df_numeric.columns[i:i+5], y_vars=['SalePrice'])

