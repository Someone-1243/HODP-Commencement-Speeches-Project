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
        title = {'font':{'size':30, 'family':"Helvetica", 'color':monochrome_colors[0]}, 'pad':{'t':100, 'r':0, 'b':0, 'l':0}},
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
                'title':{'font':{'size':24, 'family':"Helvetica", 'color':monochrome_colors[0]}},
                'font':{'size':18, 'family':"Helvetica"},
                'yanchor':'bottom'
                },
        colorscale = {'diverging':monochrome_colors},
        coloraxis = {'autocolorscale':True,
                'cauto':True,
                'colorbar':{'tickfont':{'size':14,'family':'Helvetica'}, 'title':{'font':{'size':18, 'family':'Helvetica'}}},
                }
    )
)

years = []
related = []
unrelated = []

with open("data_percentagegraph.csv", "r", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        years.append(int(row[0]))
        related.append(float(row[2]))
        unrelated.append(1 - float(row[2]))

fig = go.Figure(layout=go.Layout(barmode='stack'))

# related to wiki
fig.add_trace(go.Bar(
    x=years,
    y=related,
    name='Found in Wikipedia',
    marker_color=primary_colors[0],
))

# grey bar, not related to wiki
fig.add_trace(go.Bar(
    x=years,
    y=unrelated,
    name='Not found in Wikipedia',
    marker_color=primary_colors[4],
))

fig.update_layout(title="Percentage of Key Phrases in Wikipedia Timeline",
                xaxis={'title':{'text':'Year'}},
                yaxis={'title':{'text':'Percentage of Key Phrases'}},
                legend={'title':{'text':'Relevance'}},
                template=theme_hodp)
fig.show()
