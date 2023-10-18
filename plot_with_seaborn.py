import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
# adds matplotlib charts inline in jupyter notebooks
%matplotlib inline 

df = pd.read_csv("Book1.csv")

sns.lmplot(x='', y='', data=df)



sns.lmplot(x='', y='', data=df, fit_reg= False, hue='') #no regression line, hue adds a third variable as a category


#customize with matplotlib

plt.ylim(0,100) # sets x and y axes limits
plt.xlim(0,160)

sns.barplot(x='', y='', data=df)

sns.scatterplot(x='', y='', data=df)

df.hist(figsize=(16, 20), bins=50, xlabelsize=8, ylabelsize=8) # many histograms based on dataframe