#Using Sweetviz and ydata profiling data visualizing tool

import pandas as pd
import sweetviz as sv

df = pd.read_csv("ViewingActivity.csv")

report = sv.analyze(df)
report.show_html("eda.html") #makes savable and loadable html doc
report.show_notebook() # puts same information in the notebook

from ydata_profiling import ProfileReport 

profile = ProfileReport(df, title="eda ydata_profiling")
#minimal=True add this into ProfileReport Method for very large datasets
profile.to_file("report.html")
profile.to_notebook_iframe() # embeds the html into the notebook
