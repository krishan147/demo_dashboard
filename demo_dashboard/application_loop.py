# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df_list = [pd.DataFrame(data={'x': [1, 2, 3], 'y': [2, 4, 5]}), pd.DataFrame(data={'x': [1, 2, 3], 'y': [2, 4, 5]}),pd.DataFrame(data={'x': [1, 2, 3], 'y': [2, 4, 5]})]
output = []

i = 0
for df in df_list:

    output.append(dcc.Graph(
        id='example-graph'+str(i),
        figure={'data': [go.Bar(x=df['x'],y=df[("y")],name="yaxis")]}, className = 'six columns'))
    i = i + 1

app.layout = html.Div(children=output)


if __name__ == '__main__':
    app.run_server(debug=True)