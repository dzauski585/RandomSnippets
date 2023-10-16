import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
# %matplotlib inline # adds matplotlib charts inline in jupyter notebooks

df = pd.read_csv("Book1.csv")

sns.lmplot(x='', y='', data=df)



sns.lmplot(x='', y='', data=df, fit_reg= False, hue='') #no regression line, hue adds a third variable as a category


#customize with matplotlib

plt.ylim(0,100) # sets x and y axes limits
plt.xlim(0,160)