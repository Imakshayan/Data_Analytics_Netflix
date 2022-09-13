import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('netflix_titles.csv')
print(df)
profile = ProfileReport(df)
profile.to_file(output_file= "netflix_titles.csv")