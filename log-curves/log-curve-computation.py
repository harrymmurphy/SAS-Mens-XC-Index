"""
Computing log curves for each team
"""

import pandas as pd
import seaborn as sns
import statsmodels.api as sm 
import sklearn
# Master Dataframe
data = 'https://raw.githubusercontent.com/harrymmurphy/SAS-Mens-XC-Index/main/master-data/Master%20Data%20Sheet%20-%20Sheet1.csv'
data = pd.read_csv(data, index_col=0)
data.rename(columns={"(t=)": "xvars"}, inplace=True)
print(data.head(5))

grouped = data.groupby(data.Team)
df1 = grouped.get_group("SAS")
SAS = df1.drop(columns=['Points', 'Last','First', "Grade"])
print(SAS)
sns.scatterplot(data=SAS, x="xvars", y="Time")
