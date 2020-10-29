# !pip install pytrends

from pytrends.request import TrendReq
import pandas as pd
import time
import requests
startTime = time.time()
pytrends = TrendReq(hl='en-US', tz=360)

colnames = ["keywords"]
df = pd.read_csv("2001.csv", names=colnames)
df2 = df["keywords"].values.tolist()
df2.remove("Keywords")

groupkeywords = list(zip(*[iter(df2)]*1))
groupkeywords = [list(x) for x in groupkeywords]

dicti = {}
i = 1
for trending in groupkeywords:
    pytrends.build_payload(trending, timeframe = '2001-01-01 2001-12-31', geo = 'US')
    dicti[i] = pytrends.interest_over_time()
    i+=1

result = pd.concat(dicti, axis=1)
result.columns = result.columns.droplevel(0)
result = result.drop('isPartial', axis = 1)
result.to_csv('search_trends.csv')

# executionTime = (time.time() - startTime)
# print('Execution time in sec.: ' + str(executionTime))