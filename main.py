import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('data.csv')

profile = ProfileReport(df, title="Data Profiling Report")
profile.to_file("output.html")



