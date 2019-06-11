import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import statsmodels.api as sm


app = dash.Dash()

df_list = [pd.DataFrame(data={'x': [1,2,3,10,12,1,2,3,4,5,6], 'y': [2,4,5,1,2,1,2,3,4,5,6]}),pd.DataFrame(data={'x': [1,2,3,10,12,1,2,3,4,5,6], 'y': [2,4,5,1,2,1,2,3,4,5,6]})]
output = []
i = 0
for df in df_list:

    performance_line = pd.DataFrame(sm.nonparametric.lowess(df['x'], df['y'], frac=0.75))
    output.append([
        dcc.Graph(
            id='life-exp-vs-gdp'+str(i),
            figure={
                'data': [
                    go.Scatter(
                        x = performance_line[0],
                        y = performance_line[1],
                        mode = 'lines',
                        line = dict(
                            width=0.5
                                )
                    )
                ]+[
                    go.Scatter(
                        x=df['y'],
                        y=df['x'],
                        text=df['x'],
                        mode='markers',
                        opacity=0.7,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        }
                    )
                ],
                'layout': go.Layout(
                    xaxis={'type': 'log', 'title': 'y'},
                    yaxis={'title': 'x'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])
    i = i + 1

app.layout = html.Div(children=output)

if __name__ == '__main__':
    app.run_server()