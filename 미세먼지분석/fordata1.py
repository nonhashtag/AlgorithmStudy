import numpy as np
from numpy.random import randn
import pandas as pd
from matplotlib import pyplot as plt
from dateutil.parser import parse


df = pd.read_csv("기간별_일평균_대기환경_정보_2018년.csv",encoding='CP949',parse_dates=True,index_col=0)
data = df.reset_index()
for i in range(len(data.index)):
    if (data.iloc[i,5]==0 and data.iloc[i,6]==0 and data.iloc[i,7]==0 and data.iloc[i,8]==0 and data.iloc[i,9]==0 and data.iloc[i,10]==0):
        data.iloc[i,6] = None
        data.iloc[i,7] = None
        data.iloc[i,8] = None
        data.iloc[i,9] = None
        data.iloc[i,10] = None
dt=data.dropna()
dt1 = dt.reset_index()
dt1 = dt1.drop(["index"], axis=1)
dt1

dt1 = dt1.rename(columns=
           {"측정일자":"cdate",
            "권역코드":"acode",
            "권역명":"aname",
            "측정소코드":"scode",
            "측정소명":"sname",
            "미세먼지(㎍/㎥)":"fdust",
            "초미세먼지(㎍/㎥)":"ufdust",
            "오존(ppm)":"ozone",
            "이산화질소농도(ppm)":"nd",
            "일산화탄소농도(ppm)":"cm",
            "아황산가스농도(ppm)":"sagas"})

dt1.to_csv("data1.csv", encoding='utf-8-sig', index=False)

print(dt1)
