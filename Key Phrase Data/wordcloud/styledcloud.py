import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt

reader = csv.reader(open('namesDFtoCSV', 'r',newline='\n'))
d = {}
for k,v in reader:
    d[k] = int(v)

#Generating wordcloud. Relative scaling value is to adjust the importance of a frequency word.
#See documentation: https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py
wordcloud = WordCloud(width=900,height=500, max_words=250,relative_scaling=0.5,normalize_plurals=False,
background_color="white", min_font_size=5,colormap="inferno").generate_from_frequencies(d)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
