# do pip install plotly
import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

df = pd.read_csv('Averages.csv')
df = df.dropna()
df

fig = px.line(df, x = 'Year', y = 'Average Interest Over Time', title='Average Interest in Trending Topics')
fig.show()