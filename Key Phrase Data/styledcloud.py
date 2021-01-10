import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random

# colors
monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

reader = csv.reader(open('Key Phrase Data/wikirepeats.csv', 'r',newline='\n'))
d = {}
next(reader)
for k,v in reader:
    d[k] = int(v)

#Generating wordcloud. Relative scaling value is to adjust the importance of a frequency word.
#See documentation: https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py
wordcloud = WordCloud(width=900,height=500, max_words=250,relative_scaling=0.5,normalize_plurals=False,
background_color="white", min_font_size=5,color_func=lambda *args, **kwargs: primary_colors[random.randint(0, 3)]).generate_from_frequencies(d)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

