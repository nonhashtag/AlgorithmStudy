import numpy as np
from numpy.random import randn
import pandas as pd
from matplotlib import pyplot as plt
from dateutil.parser import parse

df = pd.read_csv("data1.csv",encoding='utf-8-sig',parse_dates=True,index_col=0)
data = df.reset_index()




for i in range(len(data.index)):
    if (data.iloc[i, 5] <= 15 and data.iloc[i,6] <= 8 and data.iloc[i, 7] < 0.02 and data.iloc[i, 8] < 0.02 and data.iloc[i, 9] < 1 and
            data.iloc[i, 10] < 0.01):
        data.loc[i, "airquality"] = "best"
    elif (data.iloc[i, 5] <= 30 and data.iloc[i,6] <= 15 and data.iloc[i, 7] < 0.03 and data.iloc[i, 8] < 0.03 and data.iloc[i, 9] < 2 and
          data.iloc[i, 10] < 0.02):
        data.loc[i, "airquality"] = "better"
    elif (data.iloc[i, 5] <= 40 and data.iloc[i,6] <= 20 and data.iloc[i, 7] < 0.06 and data.iloc[i, 8] < 0.05 and data.iloc[i, 9] < 5.5 and
          data.iloc[i, 10] < 0.04):
        data.loc[i, "airquality"] = "good"
    elif (data.iloc[i, 5] <= 50 and data.iloc[i,6] <= 25 and data.iloc[i, 7] < 0.09 and data.iloc[i, 8] < 0.06 and data.iloc[i, 9] < 9 and
          data.iloc[i, 10] < 0.05):
        data.loc[i, "airquality"] = "normal"
    elif (data.iloc[i, 5] <= 75 and data.iloc[i,6] <= 37 and data.iloc[i, 7] < 0.12 and data.iloc[i, 8] < 0.13 and data.iloc[i, 9] < 12 and
          data.iloc[i, 10] < 0.1):
        data.loc[i, "airquality"] = "bad"
    elif (data.iloc[i, 5] <= 100 and data.iloc[i,6] <= 50 and data.iloc[i, 7] < 0.15 and data.iloc[i, 8] < 0.2 and data.iloc[i, 9] < 15 and
          data.iloc[i, 10] < 0.15):
        data.loc[i, "airquality"] = "worse"
    elif (data.iloc[i, 5] <= 150 and data.iloc[i,6] <= 75 and data.iloc[i, 7] < 0.38 and data.iloc[i, 8] < 1.1 and data.iloc[i, 9] < 32 and
          data.iloc[i, 10] < 0.6):
        data.loc[i, "airquality"] = "serious"
    else:
        data.loc[i, "airquality"] = "worst"

data = data.drop(['ufdust'], axis="columns")
data.to_csv("data2_2.csv", encoding='utf-8-sig', index=False)

print(data)
