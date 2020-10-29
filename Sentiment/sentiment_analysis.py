import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

with open("sentiments.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    li = []
    year = 2000
    obj = []
    for row in reader:
        if row[0] != str(year):
            li.append(obj)
            if year == 2005:
                year = year + 2
            else:
                year = year + 1
            obj = []
        obj.append(row)
    li.append(obj)

    data = []
    for year in li:
        pos = 0
        neutral = 0
        neg = 0
        count = 0
        vals = [year[0][0]]
        for item in year:
            count = count + 1
            pos = pos + float(item[3])
            neutral = neutral + float(item[4])
            neg = neg + float(item[5])

        vals.append(pos/count)
        vals.append(neutral/count)
        vals.append(neg/count)
        data.append(vals)

pprint(data)

pos = []
neutral = []
neg = []
years = []
summed = []

for i in range(len(data)):
    years.append(int(data[i][0]))
    pos.append(data[i][1])
    neutral.append(data[i][2])
    neg.append(data[i][3])
    summed.append(pos[i] + neutral[i])

N = 20

ind = np.arange(N)    # the x locations for the groups
width = 0.5      # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, np.asarray(pos), width)
p2 = plt.bar(ind, np.asarray(neutral), width,
             bottom=pos)
p3 = plt.bar(ind, np.asarray(neg), width,
             bottom=summed)

plt.ylabel('Scores')
plt.title('Scores for Sentiment')
plt.xticks(ind, years, rotation='vertical')
plt.yticks(np.arange(0, 1, 0.1))
plt.legend((p1[0], p2[0], p3[0]), ('Pos', 'Neutral', 'Neg'), bbox_to_anchor=(1.02, 1), loc='upper left')

plt.show()
    