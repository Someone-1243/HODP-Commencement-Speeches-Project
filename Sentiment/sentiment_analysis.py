import csv
from pprint import pprint

import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

# colors
monochrome_colors = ['#251616', '#760000', '#C63F3F', '#E28073', '#F1D3CF']
primary_colors = ['#C63F3F', '#F4B436', '#83BFCC', '#455574', '#E2DDDB']

# template
theme_hodp = go.layout.Template(
    layout=go.Layout(
        title = {'font':{'size':24, 'family':"Helvetica", 'color':monochrome_colors[0]}, 'pad':{'t':100, 'r':0, 'b':0, 'l':0}},
        font = {'size':18, 'family':'Helvetica', 'color':'#717171'},
        xaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'showline': True,
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'automargin': True
                },
        yaxis = {'ticks': "outside",
                'tickfont': {'size': 14, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'title':{'font':{'size':18, 'family':'Helvetica'}, 'standoff':20},
                'showline': True,
                'automargin': True
                },
        legend = {'bgcolor':'rgba(0,0,0,0)', 
                'title':{'font':{'size':18, 'family':"Helvetica", 'color':monochrome_colors[0]}}, 
                'font':{'size':14, 'family':"Helvetica"}, 
                'yanchor':'bottom'
                },
        colorscale = {'diverging':monochrome_colors},
        coloraxis = {'autocolorscale':True, 
                'cauto':True, 
                'colorbar':{'tickfont':{'size':14,'family':'Helvetica'}, 'title':{'font':{'size':18, 'family':'Helvetica'}}},
                }
    )
)

with open("Sentiment/sentiments.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    li = []
    year = 2000
    obj = []
    for row in reader:
        if row[0] != str(year):
            li.append(obj)
            if year == 2005 or year == 2002 or year == 2000:
                year = year + 1
                li.append([[year, 0, 'none',0,0,0]])
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

# pprint(data)

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


with open('Sentiment/speech-sentiment-avg.csv', "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Year','Positive','Neutral','Negative'])
    for i in range(len(data)):
        li = []
        li.append(years[i])
        li.append(pos[i])
        li.append(neutral[i])
        li.append(neg[i])
        writer.writerow(li)

fig = go.Figure(layout=go.Layout(barmode='stack'))

fig.add_trace(go.Bar(
    x=years,
    y=pos,
    name='Positive score',
    marker_color=primary_colors[2],
))


fig.add_trace(go.Bar(
    x=years,
    y=neutral,
    name='Neutral Score',
    marker_color=primary_colors[1],
))


fig.add_trace(go.Bar(
    x=years,
    y=neg,
    name='Negative Score',
    marker_color=primary_colors[0],
))

fig.update_layout(title="Sentiment Scores for Harvard Commencement Speeches", 
                xaxis={'title':{'text':'Year'}}, 
                yaxis={'title':{'text':'Sentiment Distribution'}}, 
                legend={'title':{'text':'Sentiment'}},
                template=theme_hodp)

# fig.show()

with open("Sentiment/Wiki/wiki_sentiments.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    wiki_list = []
    year = 2001
    wiki_obj = []
    for row in reader:
        if row[0] != str(year):
            wiki_list.append(wiki_obj)
            year = year + 1
            wiki_obj = []
        wiki_obj.append(row[0:5])
    wiki_list.append(wiki_obj)

    wiki_data = [['2000',0,0,0]]
    for year_entry in wiki_list:
        pos = 0
        neutral = 0
        neg = 0
        count = 0
        vals = [year_entry[0][0]]
        for item in year_entry:
            count = count + 1
            pos = pos + float(item[2])
            neutral = neutral + float(item[3])
            neg = neg + float(item[4])

        vals.append(pos/count)
        vals.append(neutral/count)
        vals.append(neg/count)
        wiki_data.append(vals)

# pprint(wiki_data)

wiki_data.append(['2020',0,0,0])

wiki_pos = [0]
wiki_neutral = [0]
wiki_neg = [0]
wiki_years = [2000]
wiki_summed = [0]

for i in range(len(wiki_data)):
    wiki_years.append(int(wiki_data[i][0]))
    wiki_pos.append(wiki_data[i][1])
    wiki_neutral.append(wiki_data[i][2])
    wiki_neg.append(wiki_data[i][3])
    wiki_summed.append(wiki_pos[i] + wiki_neutral[i])

fig2 = go.Figure(layout=go.Layout(barmode='stack'))

fig2.add_trace(go.Bar(
    x=wiki_years,
    y=wiki_pos,
    name='Positive score',
    marker_color=primary_colors[2],
))


fig2.add_trace(go.Bar(
    x=wiki_years,
    y=wiki_neutral,
    name='Neutral Score',
    marker_color=primary_colors[1],
))


fig2.add_trace(go.Bar(
    x=wiki_years,
    y=wiki_neg,
    name='Negative Score',
    marker_color=primary_colors[0],
))

fig2.update_layout(title="Sentiment Scores per Year From Wikipedia", 
                xaxis={'title':{'text':'Year'}}, 
                yaxis={'title':{'text':'Sentiment Distribution'}}, 
                legend={'title':{'text':'Sentiment'}},
                template=theme_hodp)

# fig2.show()

pprint(wiki_data)

dataframe = []
for i in range(len(data)):
    dataframe.append(data[i] + wiki_data[i])

df = pd.DataFrame(dataframe, columns =['Years', 'Pos', 'Neutral', 'Neg', 'Wiki-Sentiment', 'Wiki-Pos', 'Wiki-Neutral', 'Wiki-Neg']) 
df = df.drop([0,1,3,6,20])
print(df) 


fig = px.scatter(
    df,
    y='Neg',
    x='Wiki-Neg',
    color_discrete_sequence=primary_colors,
    trendline='ols',
    opacity=0.8
)

fig.update_layout(
    title="Speech Sentiment vs. Year Summary Sentiment", 
    template=theme_hodp
)

fig.show()