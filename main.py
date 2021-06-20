import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as pg
import plotly as pl
import plotly.offline as po

gdp = pd.read_csv('gdp.csv')
data = dict(type='choropleth',
            locations=gdp['CODE'],
            z=gdp['GDP (BILLIONS)'],
            text=gdp['COUNTRY'])
layout = dict(title='GDP GEO-PLOT', geo=dict(projection={'type': 'hammer'}))
x = pg.Figure(data=[data], layout=layout)
print(po.plot(x))
