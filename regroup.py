import numpy as np 
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go 
import plotly.offline as pyo
import plotly.figure_factory as ff
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

np.random.seed(42)

data_1_02_x = np.random.randint(1,101,100) 
data_1_02_y = np.random.randint(1,101,100) 

data_1_02_x_exc = np.random.randn(1000) 
data_1_02_y_exc = np.random.rand(1000)

app = dash.Dash()

app.layout = html.Div(id = 'overall',
                      children = [html.H1(children = 'Second round of Ploty!!!!'),
                                  html.Div(id = 'class_1_02', 
                                           children = [html.H3(children = '***** Class 1-02 ScatterPlots'),
                                                       dcc.Graph( id = 'plot1',
                                                           figure =
                                                          {'data' : [go.Scatter(x = data_1_02_x, 
                                                                                y = data_1_02_y, 
                                                                                mode = 'markers', 
                                                                                marker = dict(size = 12, 
                                                                                               color = 'rgb(51,204,153)', 
                                                                                            #    symbol = 'pentagon',
                                                                                               symbol = 'octagon',
                                                                                               line = dict(width = 2)
                                                                                               ))],
                                                           'layout': go.Layout(title = '1-02 ScatterPlot class',
                                                                               xaxis = {'title': 'hello'},
                                                                               yaxis = {'title': 'y-axis'},
                                                                               hovermode = 'closest')
                                                          }
                                                       )],style={'marginLeft': '80px'}),
                                    html.Div(id = 'class_1-02',
                                             children = [html.H3(children = '***** Class 1-02 ScatterPlots Exercises'),
                                                         dcc.Graph( id = 'plot2',
                                                             figure = dict(
                                                                 data = [go.Scatter(x = data_1_02_x_exc,
                                                                                    y = data_1_02_y_exc,
                                                                                    mode = 'markers',
                                                                                    marker = dict(size = 10, 
                                                                                                  color = 'purple',
                                                                                                  symbol = 'x') 
                                                                 )],
                                                                 layout = go.Layout(dict(title = '1-02 ScatterPlot class Exercise', 
                                                                                          xaxis = dict(title = 'x'),
                                                                                          yaxis = dict(title = 'y'),
                                                                                          hovermode = 'closest')
                                                                 )
                                                             )
                                                         )
                                                         ], style={'marginLeft': '80px'}),
                                    html.Div(id = 'class_1-03', 
                                             children = [html.H3(children = '***** Class 1-03 LineChart'),
                                                         dcc.Graph(id = 'plot3',
                                                                   figure = dict(data = [],
                                                                                 layout = go.Layout(dict(title = '1-03 Line Chart class')
                                                                                                    )
                                                                                )
                                                                                )], style={'marginLeft': '80px'}),
dcc.Input(
    id = 'input1',
    value = 1,
    style = {'fontSize': 28}
        )], style={'marginLeft': '40px'}

)

if __name__ == '__main__':
    app.run()