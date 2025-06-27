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

data_1_03_x = np.linspace(0,1,100)
data_1_03_y = np.random.randn(100)

df_103 = pd.read_csv('SourceData/nst-est2017-alldata.csv', header = 0)
df_sub_103 = df_103.loc[df_103.DIVISION == '1',]
df_sub_103.set_index('NAME', inplace= True)
df_sub_103 = df_sub_103.loc[:,[i for i in df_sub_103.columns if i.startswith('POP')]]

df_103_exc = pd.read_csv('data/2010YumaAZ.csv', header = 0)

df_1_04 = pd.read_csv('Data/2018WinterOlympics.csv', header = 0)

df_104_exc = pd.read_csv('data/mocksurvey.csv', header = 0)

app = dash.Dash()

app.layout = html.Div(id = 'Day1- overall',
                      children = [html.H1(children = 'Day 1: Second round of Ploty!!!!'),
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
                                    html.Div(id = 'class_1-02_exe',
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
                                                         )], style={'marginLeft': '80px'}),
                                    html.Div(id = 'class_1_03_part1', 
                                            children = [html.H3(children = '***** Class 1-03 LineChart part1'),
                                                         dcc.Graph(id = 'plot3',
                                                                   figure = dict(data = [go.Scatter(dict(x = data_1_03_x,
                                                                                                         y = data_1_03_y +5,
                                                                                                         mode = 'lines',
                                                                                                         name = '+5',
                                                                                                         marker = dict(color = 'red'))),
                                                                                        go.Scatter(dict(x = data_1_03_x,
                                                                                                         y = data_1_03_y,
                                                                                                         mode = 'markers',
                                                                                                         name = 'normal',
                                                                                                         marker = dict(color = 'green'))),
                                                                                         go.Scatter(dict(x = data_1_03_x,
                                                                                                         y = data_1_03_y - 5 ,
                                                                                                         mode = 'lines',
                                                                                                         name = '-5',
                                                                                                         marker = dict(color ='pink')))                ],
                                                                                 layout = go.Layout(dict(title = '1-03 Line Chart class', 
                                                                                                         xaxis = dict(title = 'hello'), 
                                                                                                         yaxis = dict(title = 'well do'),
                                                                                                         hovermode = 'closest')
                                                                                                    )
                                                                                )
                                                                                )], style={'marginLeft': '80px'}),
                                    html.Div(id = 'class_1_03_part2', 
                                            children = [html.H3(children = '***** Class 1-03 LineChart part2'),
                                                        dcc.Graph(id = 'plot4', 
                                                                  figure = dict(data = [go.Scatter(x = df_sub_103.columns,
                                                                                                   y = df_sub_103.loc[i], 
                                                                                                   mode = 'lines', 
                                                                                                   name = i)
                                                                                        for i in df_sub_103.index],
                                                                                 layout = go.Layout(dict(title = '1-03 Line Chart class Part 2')))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                    html.Div(id = 'class_1_03_exec', 
                                            children = [html.H3(children = '***** Class 1-03 LineChart Exercises'),
                                                        dcc.Graph(id = 'plot5', 
                                                                  figure = dict(data = [go.Scatter(x = df_103_exc.loc[df_103_exc.DAY == i,'LST_TIME'],
                                                                                                   y = df_103_exc.loc[df_103_exc.DAY == i,'T_HR_AVG'], 
                                                                                                   mode = 'lines', 
                                                                                                   name = i)
                                                                                        for i in df_103_exc.DAY.drop_duplicates()],
                                                                                 layout = go.Layout(dict(title = '1-03 Line Chart class Exercises',
                                                                                                         xaxis = dict(title = 'Time'),
                                                                                                         yaxis = dict(title = 'Avg_temp'))))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                    html.Div(id = 'class_1_04', 
                                            children = [html.H3(children = '***** Class 1-04 Bar chart'),
                                                        dcc.Graph(id = 'plot6', 
                                                                  figure = dict(data = [go.Bar(x = df_1_04.NOC,
                                                                                               y = df_1_04.Total)
                                                                                        ],
                                                                                 layout = go.Layout(dict(title = '1-04 Bar Chart class',
                                                                                                         xaxis = dict(title = 'Nation'),
                                                                                                         yaxis = dict(title = 'Total metals'))))
                                                         ),
                                                        dcc.Graph(id = 'plot7', 
                                                                   figure = dict(data = [go.Bar(x = df_1_04.NOC,
                                                                                                y = df_1_04[i],
                                                                                                name = i )
                                                                                         for i in ['Gold', 'Silver', 'Bronze']],
                                                                                layout = go.Layout(dict(title = '1-04 Bar Chart class part2',
                                                                                                        xaxis = dict(title = 'Nationality'),
                                                                                                        yaxis = dict(title = 'Total Metals'))))),
                                                        dcc.Graph(id = 'plot8', 
                                                                   figure = dict(data = [go.Bar(x = df_1_04.NOC,
                                                                                                y = df_1_04[i],
                                                                                                name = i
                                                                                                )
                                                                                         for i in ['Gold' , 'Silver', 'Bronze']],
                                                                                layout = go.Layout(dict(title = '1-04 Bar Chart class part3',
                                                                                                        xaxis = dict(title = 'Nationality'),
                                                                                                        yaxis = dict(title = 'Total Metals'),
                                                                                                        barmode = 'stack'))))
                                                                   ], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_04_exec', 
                                            children = [html.H3(children = '***** Class 1-04 BarChart Exercises'),
                                                        dcc.Graph(id = 'plot9', 
                                                                  figure = dict(data = [go.Bar(x = df_104_exc.iloc[:,0],
                                                                                               y = df_104_exc.iloc[:,i],
                                                                                               name = df_104_exc.columns[i]
                                                                                              )
                                                                                        for i in range(1,df_104_exc.shape[1])],
                                                                                 layout = go.Layout(dict(title = '1-03 Line Chart class Exercises',
                                                                                                         xaxis = dict(title = 'Questions'),
                                                                                                         yaxis = dict(title = 'Percentage'),
                                                                                                         barmode = 'stack')))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_04_exec_sub', 
                                            children = [html.H3(children = '***** Class 1-04 BarChart Exercises extra'),
                                                        dcc.Graph(id = 'plot9', 
                                                                  figure = dict(data = [go.Bar(y= df_104_exc.iloc[:,0],
                                                                                               x = df_104_exc.iloc[:,i],
                                                                                               name = df_104_exc.columns[i],
                                                                                               orientation='h'
                                                                                              )
                                                                                        for i in range(1,df_104_exc.shape[1])],
                                                                                 layout = go.Layout(dict(title = '1-03 Line Chart class Exercises extra',
                                                                                                         yaxis = dict(title = 'Questions'),
                                                                                                         xaxis = dict(title = 'Percentage'),
                                                                                                         barmode = 'stack'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),


                                        dcc.Input( id = 'input1', value = 1, style = {'fontSize': 28})
                                        ], style={'marginLeft': '40px'}
)

if __name__ == '__main__':
    app.run()
