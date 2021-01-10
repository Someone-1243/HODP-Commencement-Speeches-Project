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
        title = {'font':{'size':28, 'family':"Helvetica", 'color':monochrome_colors[0]}, 'pad':{'t':100, 'r':0, 'b':0, 'l':0}},
        font = {'size':22, 'family':'Helvetica', 'color':'#717171'},
        xaxis = {'ticks': "outside",
                'tickfont': {'size': 18, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'showline': True,
                'title':{'font':{'size':22, 'family':'Helvetica'}, 'standoff':20},
                'automargin': True
                },
        yaxis = {'ticks': "outside",
                'tickfont': {'size': 18, 'family':"Helvetica"},
                'showticksuffix': 'all',
                'showtickprefix': 'last',
                'title':{'font':{'size':22, 'family':'Helvetica'}, 'standoff':20},
                'showline': True,
                'automargin': True
                },
        legend = {'bgcolor':'rgba(0,0,0,0)', 
                'title':{'font':{'size':22, 'family':"Helvetica", 'color':monochrome_colors[0]}}, 
                'font':{'size':20, 'family':"Helvetica"}, 
                'yanchor':'bottom'
                },
        colorscale = {'diverging':monochrome_colors},
        coloraxis = {'autocolorscale':True, 
                'cauto':True, 
                'colorbar':{'tickfont':{'size':18,'family':'Helvetica'}, 'title':{'font':{'size':22, 'family':'Helvetica'}}},
                }
    )
)

data = []
azure_data = []

with open("Sentiment/Second_API/csv/sentiment2_averages.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    li = []
    for row in reader:
        li.append(row)

    for row in li:
        year = row[0]
        pos = row[5]
        neutral = row[6]
        neg = row[7]

        vals = [year]
        vals.append(pos)
        vals.append(neutral)
        vals.append(neg)
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

fig.update_layout(title="Sentiment Scores for Harvard Commencement Speeches<br>(Word-Processing API)", 
                xaxis={'title':{'text':'Year'}}, 
                yaxis={'title':{'text':'Sentiment Distribution'}}, 
                legend={'title':{'text':'Sentiment'}},
                template=theme_hodp)

fig.show()

wiki_pos = [0]
wiki_neutral = [0]
wiki_neg = [0]
wiki_years = [2000]
wiki_summed = [0]

with open("Sentiment/Second_API/wiki_sentiments2_averages.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    year = 2001
    wiki_data = [['2000',0,0,0]]
    for row in reader:
        wiki_data.append(row)

    for row in wiki_data:
        wiki_years.append(row[0])
        wiki_pos.append(row[1])
        wiki_neutral.append(row[2])
        wiki_neg.append(row[3])
        wiki_summed.append(row[1]+row[2])

# pprint(wiki_data)

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

fig2.update_layout(title="Sentiment Scores per Year From Wikipedia<br>(Word-Processing API)", 
                xaxis={'title':{'text':'Year'}}, 
                yaxis={'title':{'text':'Sentiment Distribution'}}, 
                legend={'title':{'text':'Sentiment'}},
                template=theme_hodp)

fig2.show()

pprint(wiki_data)

dataframe = []
for i in range(len(data)):
    dataframe.append(data[i] + wiki_data[i])

df = pd.DataFrame(dataframe, columns =['Years', 'Positive Sentiment in Speech', 'Neutral', 'Negative Sentiment in Speech', 'Wiki-Sentiment', 'Wiki-Pos', 'Wiki-Neutral', 'Negative Sentiment of Wikipedia Summary']) 
df = df.drop([0,1,3,6])
print(df) 


fig3 = px.scatter(
    df,
    y='Negative Sentiment in Speech',
    x='Negative Sentiment of Wikipedia Summary',
    color_discrete_sequence=primary_colors,
    trendline='ols',
    opacity=0.8
)

fig3.update_layout(
    title="Negative Speech Sentiment vs. Negative Year Summary Sentiment <br>(Word-Processing API)", 
    template=theme_hodp
)

fig3.show()
