#  do pip install pytrends before starting
import pandas as pd
from pytrends.request import TrendReq

pytrend = TrendReq(hl='en-GB', tz=360)

colnames = ["keywords"]
df = pd.read_csv("years.csv", names=colnames)
df2 = df["keywords"].values.tolist()

dataset = []

for x in range(0,len(df2)):
     keywords = [df2[x]]
     pytrend.build_payload(
     kw_list=keywords,
     cat=0,
# change based on timeframe you want
     timeframe='2020-01-01 2020-12-31',
     geo='US')
     data = pytrend.interest_over_time()
     if not data.empty:
          data = data.drop(labels=['isPartial'],axis='columns')
          dataset.append(data)

result = pd.concat(dataset, axis=1)
# creates a new csv that contains the term and the interest over time
result.to_csv('search_trends.csv')