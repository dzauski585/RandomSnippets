import pandas as pd #pandas library

df = pd.read_csv("Book1.csv") # read the data from csv other methods for other formats

df.shape # attribute returns a colums, rows, total

df.head() # shows the first 5 rows and corresponding columns
df.tail() # last 5 rows. Can place numbers in the () to get more or less rows

df.describe() # gives the following information: count, mean, std, min, 25%, 50%, 75%, max 

for col in df.columns: # loop that prints all of the columns titles since some of the other pandas tools truncate the lists
    print(col)