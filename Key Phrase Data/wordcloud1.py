import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

reader = csv.reader(open('Key Phrase Data/wikirepeats.csv', 'r',newline='\n'))
d = {}
next(reader)
for k,v in reader:
    d[k] = int(v)

#Generating wordcloud. Relative scaling value is to adjust the importance of a frequency word.
#See documentation: https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py
wordcloud = WordCloud(width=900,height=500, max_words=1628,relative_scaling=1,normalize_plurals=False).generate_from_frequencies(d)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

