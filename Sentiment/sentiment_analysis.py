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

with open("sentiments.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    li = []
    year = 2000
    obj = []
    for row in reader:
        if row[0] != str(year):
            li.append(obj)
            if year == 2005 or year == 2002 or year == 2000:
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

fig.show()
