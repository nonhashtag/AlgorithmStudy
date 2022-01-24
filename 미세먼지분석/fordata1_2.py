import numpy as np
from numpy.random import randn
import pandas as pd
from matplotlib import pyplot as plt
from dateutil.parser import parse

df = pd.read_csv("data1.csv",encoding='utf-8-sig',parse_dates=True,index_col=0)
data = df.reset_index()


for i in range(len(data.index)):
    data.loc[i, "ozone(ug/m^3)"] = (48/22.4)*1000 * data.loc[i, "ozone"]
    data.loc[i, "nd(ug/m^3)"] = (46/22.4)*1000 * data.loc[i, "nd"]
    data.loc[i, "cm(ug/m^3)"] = (28/22.4)*1000 * data.loc[i, "cm"]
    data.loc[i, "sagas(ug/m^3)"] = (64/22.4)*1000 * data.loc[i, "sagas"]

    data.loc[i, "fdust^2"] = data.loc[i, "fdust"] * data.loc[i, "fdust"]
    data.loc[i, "ufdust^2"] = data.loc[i, "ufdust"] * data.loc[i, "ufdust"]
    data.loc[i, "ozone^2"] = data.loc[i, "ozone(ug/m^3)"] * data.loc[i, "ozone(ug/m^3)"]
    data.loc[i, "nd^2"] = data.loc[i, "nd(ug/m^3)"] * data.loc[i, "nd(ug/m^3)"]
    data.loc[i, "cm^2"] = data.loc[i, "cm(ug/m^3)"] * data.loc[i, "cm(ug/m^3)"]
    data.loc[i, "sagas^2"] = data.loc[i, "sagas(ug/m^3)"] * data.loc[i, "sagas(ug/m^3)"]

data.to_csv("data2.csv", encoding='utf-8-sig', index=False)
print(data)

