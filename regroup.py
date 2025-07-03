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
from plotly import tools
import json
import base64

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

df_105 = pd.read_csv('data/mpg.csv', header = 0)

data_1_06 = [i for i in np.random.randint(1,101, 20)]
data_1_06.append(90)
data_1_06_sub = [i for i in np.random.randint(1,101, 20)]
data_1_06_sub.append(160)

df_106 = pd.read_csv('data/abalone.csv', header = 0)

df_107 = pd.read_csv('data/mpg.csv', header = 0)

df_107_2 = pd.read_csv('data/arrhythmia.csv', header = 0)

df_107_3  = pd.read_csv('/Users/pangrui/Desktop/Ploty_class/Plotly_udmy_class/Data/FremontBridgeBicycles.csv', header= 0)

df_107_3['Date'] = pd.to_datetime(df_107_3.Date)
df_107_3['new_date'] = df_107_3['Date'].dt.date
df_107_3['Hr'] = df_107_3['Date'].dt.time

df_107_3_final = df_107_3.groupby('Hr').agg({'Fremont Bridge West Sidewalk': 'sum', 'Fremont Bridge East Sidewalk': 'sum'}).reset_index()

df_107_exc = pd.read_csv('data/abalone.csv')

data_108 = [np.random.randn(1000)]
label = ['Normal Distribution']

data_108_2 =  [np.random.randn(1000)-5, np.random.randn(1000)-2, np.random.randn(1000), np.random.randn(1000) +2] 

df_108_exc = pd.read_csv('data/iris.csv', header= 0)

df_109 = pd.read_csv('data/2010SantaBarbaraCA.csv', header = 0)
df_109_2 = pd.read_csv('data/2010YumaAz.csv', header = 0)
df_109_3 = pd.read_csv('data/2010SitkaAK.csv', header = 0)

plot_109 = tools.make_subplots(rows =1, cols = 3, 
                               subplot_titles = ['SB CA', 'Yuma AZ', 'SIT AK'],
                               shared_yaxes = True)
plot_109.append_trace(go.Heatmap(x =df_109.DAY, y =df_109.LST_TIME, z = df_109.T_HR_AVG.tolist(), zmin = 5, zmax = 40,
                                 colorscale = 'Jet', name='Heatmap 1'), 1, 1)
plot_109.append_trace(go.Heatmap(x =df_109_2.DAY, y =df_109_2.LST_TIME, z = df_109_2.T_HR_AVG.tolist(), zmin = 5, zmax = 40,
                                 colorscale = 'Jet', name='Heatmap 2'), 1, 2)
plot_109.append_trace(go.Heatmap(x =df_109_3.DAY, y =df_109_3.LST_TIME, z = df_109_3.T_HR_AVG.tolist(), zmin = 5, zmax = 40,
                                 colorscale = 'Jet', name='Heatmap 3'), 1, 3)

df_109_exc = pd.read_csv('data/flights.csv', header= 0)

df_2_08 = pd.read_csv('data/gapminderDataFiveYear.csv', header= 0)

df_2_09 = pd.read_csv('data/mpg.csv', header = 0)

data_2_13 = pd.DataFrame({'color': ['red', 'red', 'red', 'blue','blue','blue', 'yellow', 'yellow', 'yellow'],
             'value': [1,2,3,1,2,3,1,2,3]})

df_2_13 = pd.read_csv('data/wheels.csv', header = 0)

def encode_image(file_name):
    ecode = base64.b64encode(open(file_name, 'rb').read())
    return f'data:image/png;base64,{ecode.decode()}'

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
                                                                                 layout = go.Layout(dict(title = '1-04 BarChart Chart class Exercises',
                                                                                                         xaxis = dict(title = 'Questions'),
                                                                                                         yaxis = dict(title = 'Percentage'),
                                                                                                         barmode = 'stack')))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_04_exec_sub', 
                                            children = [html.H3(children = '***** Class 1-04 BarChart Exercises extra'),
                                                        dcc.Graph(id = 'plot10', 
                                                                  figure = dict(data = [go.Bar(y= df_104_exc.iloc[:,0],
                                                                                               x = df_104_exc.iloc[:,i],
                                                                                               name = df_104_exc.columns[i],
                                                                                               orientation='h'
                                                                                              )
                                                                                        for i in range(1,df_104_exc.shape[1])],
                                                                                 layout = go.Layout(dict(title = '1-04 BarChart Chart class Exercises extra',
                                                                                                         yaxis = dict(title = 'Questions'),
                                                                                                         xaxis = dict(title = 'Percentage'),
                                                                                                         barmode = 'stack'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_05', 
                                            children = [html.H3(children = '***** Class 1-05 Bubble Chart '),
                                                        dcc.Graph(id = 'plot11', 
                                                                  figure = dict(data = [go.Scatter(x= df_105.horsepower,
                                                                                                  y =df_105.mpg ,
                                                                                                  text = df_105['name'],
                                                                                                  mode = 'markers',
                                                                                                  marker = dict(size = df_105.weight /100, 
                                                                                                                color = df_105.cylinders,
                                                                                                                showscale = True))
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-05 Bubble Chart class',
                                                                                                         xaxis = dict(title = 'horsepower'),
                                                                                                         yaxis = dict(title = 'mpg'), 
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_05_exercise', 
                                            children = [html.H3(children = '***** Class 1-04 Bubble Chart Exercise'),
                                                        dcc.Graph(id = 'plot12', 
                                                                  figure = dict(data = [go.Scatter(x= df_105.displacement,
                                                                                                   y= df_105.acceleration ,
                                                                                                   text = df_105['name'],
                                                                                                   mode = 'markers',
                                                                                                   marker = dict(size = df_105.cylinders * 1.5
                                                                                                                # ,color = df_105.cylinders,
                                                                                                                # showscale = True
                                                                                                                ))
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-05 Bubble Chart class Exercise',
                                                                                                         xaxis = dict(title = 'displacement'),
                                                                                                         yaxis = dict(title = 'acceleration'), 
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_06', 
                                            children = [html.H3(children = '***** Class 1-06 Box Chart '),
                                                        dcc.Graph(id = 'plot13', 
                                                                  figure = dict(data = [go.Box(y= data_1_06,
                                                                                               boxpoints = 'all', # display the original data points will not display outliers on the box plot!
                                                                                                jitter = 0.3, # spread them out so they all appear
                                                                                               pointpos = -1.8 # pffset them to the left of the box
                                                                                                  ),
                                                                                        go.Box(y= data_1_06_sub,
                                                                                               boxpoints = 'outliers',  # display outliers as wll
                                                                                               name = 'ote'
                                                                                                  )
                                                                                        
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-06 BOX Chart class',
                                                                                                         
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_06_sub', 
                                            children = [html.H3(children = '***** Class 1-06 Box Chart sub'),
                                                        dcc.Graph(id = 'plot14', 
                                                                  figure = dict(data = [go.Box(y= data_1_06,
                                                                                               name = 'abc',
                                                                                               boxpoints = 'outliers'                                         
                                                                                                ),
                                                                                        go.Box(y= [i+15 for i in data_1_06_sub] ,
                                                                                               boxpoints = 'outliers',
                                                                                               name = 'ote'
                                                                                                  )
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-06 BOX Chart class sub',
                                                                                                         
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_06_Exercise', 
                                            children = [html.H3(children = '***** Class 1-06 Box Chart Exercise'),
                                                        dcc.Graph(id = 'plot15', 
                                                                  figure = dict(data = [go.Box(y= np.random.choice(df_106.rings,10,replace = True),
                                                                                               name = 'With_replace',
                                                                                               boxpoints = 'outliers'                                         
                                                                                                ),
                                                                                        go.Box(y= np.random.choice(df_106.rings,10,replace = True),
                                                                                               boxpoints = 'outliers',
                                                                                               name = 'With_out_replacement'
                                                                                                  )
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-06 BOX Chart class Exercise',
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_07_Class', 
                                            children = [html.H3(children = '***** Class 1-07 Histograms Chart Class'),
                                                        dcc.Graph(id = 'plot16', 
                                                                  figure = dict(data = [go.Histogram(dict(x = df_107.mpg))
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-07 Histograms Chart class',
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_07_Class Part 2', 
                                            children = [html.H3(children = '***** Class 1-07 Histograms Chart Class Part 2'),
                                                        dcc.Graph(id = 'plot17', 
                                                                  figure = dict(data = [go.Histogram(dict(x = df_107.mpg, 
                                                                                                          xbins = dict(start = 8, 
                                                                                                                       end = 50, 
                                                                                                                       size = 6)))
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-07 Histograms Chart class part 2',
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_07_Class Part 3', 
                                            children = [html.H3(children = '***** Class 1-07 Histograms Chart Class Part 3'),
                                                        dcc.Graph(id = 'plot18', 
                                                                  figure = dict(data = [go.Histogram(dict(x = df_107.mpg, 
                                                                                                          xbins = dict(start = 8, 
                                                                                                                       end = 50, 
                                                                                                                       size = 1)))
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-07 Histograms Chart class part 3',
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_07_Class Part 4', 
                                            children = [html.H3(children = '***** Class 1-07 Histograms Chart Class Part 4'),
                                                        dcc.Graph(id = 'plot19', 
                                                                  figure = dict(data = [go.Histogram(dict(x = df_107_2.loc[df_107_2.Sex ==0, 'Height'], 
                                                                                                          opacity  = 0.75, 
                                                                                                          name = 'Male'
                                                                                                         )),
                                                                                        go.Histogram(dict(x = df_107_2.loc[df_107_2.Sex != 0, 'Height'], 
                                                                                                          opacity = 0.75, 
                                                                                                          name = 'Female'))
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-07 Histograms Chart class part 4',
                                                                                                         barmode = 'overlay',
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_07_Class Part 5', 
                                            children = [html.H3(children = '***** Class 1-07 Histograms Chart Class Part 5'),
                                                        dcc.Graph(id = 'plot20', 
                                                                  figure = dict(data = [go.Bar(dict(x = df_107_3_final.Hr,
                                                                                                    y = df_107_3_final['Fremont Bridge West Sidewalk'], 
                                                                                                          width = 1,
                                                                                                          name = 'South Bound'
                                                                                                         )),
                                                                                        go.Bar(dict(x = df_107_3_final.Hr,
                                                                                                    y = df_107_3_final['Fremont Bridge East Sidewalk'], 
                                                                                                    width = 1,
                                                                                                    name = 'North Bound'))
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-07 Histograms Chart class part 5',
                                                                                                         barmode = 'stack',
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_07_Class Exercise', 
                                            children = [html.H3(children = '***** Class 1-07 Histograms Chart Exercise'),
                                                        dcc.Graph(id = 'plot21', 
                                                                  figure = dict(data = [go.Histogram(dict(x = df_107_exc.length,
                                                                                                          xbins = dict(start = 0, 
                                                                                                                     end = 1, 
                                                                                                                     size = 0.02)
                                                                                                         ))
                                                                                        
                                                                                              ],
                                                                                 layout = go.Layout(dict(title = '1-07 Histograms Chart Exercise',
                                                                                                         hovermode = 'closest'
                                                                                                         )))
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_08_Class', 
                                            children = [html.H3(children = '***** Class 1-08 Distplot Chart'),
                                                        dcc.Graph(id = 'plot22', 
                                                                  figure = ff.create_distplot(data_108,
                                                                                              group_labels= label,
                                                                                              show_rug=True
                                                                                             )
                                                                                 
                                                         )], 
                                                    style={'marginLeft': '80px'}),

                                        html.Div(id = 'class_1_08_Class Part2', 
                                            children = [html.H3(children = '***** Class 1-08 Distplot Chart part2'),
                                                        dcc.Graph(id = 'plot23', 
                                                                  figure = ff.create_distplot(data_108_2,
                                                                                              group_labels= ['part1', 'part2', 'part3', 'part4'],
                                                                                              show_rug=True,
                                                                                              bin_size=0.3
                                                                                             )
                                                                                 
                                                         )], 
                                                    style={'marginLeft': '80px'}),

                                        html.Div(id = 'class_1_08_Class Exercise', 
                                            children = [html.H3(children = '***** Class 1-08 Distplot Chart Exercise'),
                                                        dcc.Graph(id = 'plot24', 
                                                                  figure = ff.create_distplot([df_108_exc.loc[df_108_exc['class'].str.contains('setosa'), 'petal_length'],
                                                                                               df_108_exc.loc[df_108_exc['class'].str.contains('versic'), 'petal_length'],
                                                                                               df_108_exc.loc[df_108_exc['class'].str.contains('virgin'), 'petal_length']],
                                                                                              group_labels= ['Setosa', 'Versicolor', 'Virginica'],
                                                                                              show_rug=True                                                                                             )              
                                                         )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_09_Class', 
                                            children = [html.H3(children = '***** Class 1-09 Heatmap Chart'),
                                                        dcc.Graph(id = 'plot25', 
                                                                  figure = dict(data = [go.Heatmap(dict(x =df_109.DAY , 
                                                                                                        y =df_109.LST_TIME,
                                                                                                        z = df_109.T_HR_AVG.tolist(), 
                                                                                                        colorscale = 'Jet'
                                                                                                        ))],
                                                                                layout = go.Layout(dict(title = 'Class 1-09 Heatmap Chart', 
                                                                                                        xaxis = dict(title = 'hello')))
                                                                                
                                                                  )
                                                                  )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_09_Class part 2', 
                                            children = [html.H3(children = '***** Class 1-09 Heatmap Chart part 2'),
                                                        dcc.Graph(id = 'plot26', 
                                                                  figure = plot_109
                                                                  )], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_1_09_Class Exercise', 
                                            children = [html.H3(children = '***** Class 1-09 Heatmap Chart Exercise'),
                                                        dcc.Graph(id = 'plot27', 
                                                                  figure = dict(data = [go.Heatmap(x = df_109_exc.year,
                                                                                                   y = df_109_exc.month,
                                                                                                   z = df_109_exc.passengers.tolist())],
                                                                                layout = go.Layout(dict(title = 'Class 1-09 Heatmap Chart Exercise'))
                                                                                )
                                                                  )], 
                                                    style={'marginLeft': '80px'}),

                                        html.H2('***** Core Components!!!!'),
                                        html.Label('---Slider---'),
                                        dcc.Slider(min = -5, max = 10, step = 1,
                                                   marks = {i: i for i in range(-5,11)},
                                                   value = 2), 
                                        html.Label('---Dropdown---'),
                                        dcc.Dropdown(options = [{'label': 'nba', 'value': 'Kobe'},
                                                                {'label': 'cba', 'value': 'Yaoming'},
                                                                {'label': 'wnba', 'value': 'Sabrina'}],
                                                    value = 'Kobe'),
                                        html.Label('---Multi Select Dropdown---'),
                                        dcc.Dropdown(id = 'dropdown1',
                                                     options = [{'label': 'New York City', 'value': 'NYC'},
                                                                {'label': 'Seattle', 'value': 'SEA'},
                                                                {'label': 'Madison', 'value': 'MAD'}],
                                                    value = ['NYC', 'SEA'],
                                                    multi = True),
                                        html.Label('---Radio Items---'),
                                        dcc.RadioItems(options = [{'label': 'Costco', 'value': 'COT'},
                                                                {'label': 'Tesla', 'value': 'TSA'},
                                                                {'label': 'United Health', 'value': 'UNH'}],
                                                    value = 'UNH'),
                                        html.Label('---Check List---'),
                                        dcc.Checklist(options = [{'label': 'Mac book', 'value': 'pro'},
                                                                 {'label': 'Iphone', 'value': '18'},
                                                                 {'label': 'Ipad', 'value': 'mini'}],
                                                        value = ['pro'],
                                                        labelStyle={'display': 'block'}),
                                        html.Label('---Input---'),
                                        dcc.Input( id = 'input1', value = 1 ),
                                        html.Div(id = 'class_2_07_Class_callback', 
                                            children = [html.H3(children = '***** Class 2-07 Callback Chart'),
                                                        html.Div(id = 'class_2_07')
                                                        ], 
                                                    style={'marginLeft': '80px'}),
                                        html.Div(id = 'class_2_08_Multiple Inputs', 
                                                 children = [html.H3(children = '***** Class 2-08 Multiple Input'),
                                                             dcc.Dropdown(id = 'drop_class_2_08', 
                                                                          options = [{'label': f'{i}', 'value': i} 
                                                                                     for i in df_2_08.year.drop_duplicates()],
                                                                          value = df_2_08.year.min()),
                                                             dcc.Graph(id = 'class_2_08')]),

                                        html.Div(id = 'class_2_09_Multiple outputs', 
                                                 children = [html.H3(children = '***** Class 2-09 Multiple Outputs'),
                                                             dcc.Dropdown(id = 'drop_class_2_09_sub1', 
                                                                          options = [dict(label = i, value = i)
                                                                                     for i in df_2_09.columns.values],
                                                                          value = df_2_09.columns[0]),
                                                            dcc.Dropdown(id = 'drop_class_2_09_sub2'),
                                                             dcc.Graph(id = 'class_2_09')]),

                                        html.Div(id = 'class_2_10_Interactive Exercise', 
                                                 children = [html.H3(children = '***** Class 2-10 Interactive Exercise'),
                                                             dcc.RangeSlider(id = 'Slider_class_2_10',
                                                                             min = -5,
                                                                             max = 10,
                                                                             step = 1,
                                                                             marks = {i:str(i) for i in range(-5,11)},
                                                                             value = [-1, 3],
                                                                             allowCross=False),
                                                             html.Div(id = 'class_2_10_result')
                                                            ]),
                                        html.Div(id = 'class_2_12_State call back Data', 
                                                 children = [html.H3(children = '***** Class 2-12 Hover Data'),
                                                             dcc.Input(id = 'class_2_12_input', 
                                                                       value = 1), 
                                                             html.Button(id = 'class_2_12_button',
                                                                         n_clicks = 0,
                                                                         children = 'Run'), 
                                                             html.Div(id = 'class_2_12_out')
                                                            ]),
                                         html.Div(id = 'class_2_13_Hover Data Exercise', 
                                                 children = [html.H3(children = '***** Class 2-13 Hover Data'),
                                                             html.Div(children = [
                                                                 dcc.Graph(id = 'class_2_13',
                                                                       figure =dict(data = [go.Scatter(x = data_2_13.color,
                                                                                                       y = data_2_13.value,
                                                                                                       mode = 'markers')],
                                                                                layout = go.Layout(title = 'Class 2-13 Hover Data',
                                                                                                   xaxis = dict(title = 'Color'),
                                                                                                   yaxis = dict(title = 'value'))),
                                                                                                   style = dict(width = '30%',
                                                                                                                float = 'left')),
                                                                html.Pre(id = 'class_2_13_out', style = dict(width = '30%', paddingTop = 35)),
                                                                html.Img(id = 'class_2_13_img', style = dict(width = '30%', 
                                                                                                         float = 'right',
                                                                                                         paddingTop = 35))],
                                                                 style = {'display': 'flex', 'justifyContent': 'space-between', 'height': '400px'})
                                                             
                                                            ])
                                        ],
                                          style={'marginLeft': '40px'}
)

@app.callback(Output(component_id = 'class_2_07', component_property = 'children'),
              [Input(component_id = 'dropdown1', component_property = 'value')],
              prevent_initial_call = True
)

def class2_07(c207):
    t1 = f"Today we are going to go to {', '.join(c207)}!!!!!"
    return t1


@app.callback(Output(component_id = 'class_2_08', component_property = 'figure'),
              [Input(component_id = 'drop_class_2_08',component_property = 'value')],
              prevent_initial_call = True)

def class_2_08(c208):
    temp1 = df_2_08.loc[df_2_08.year == c208,]
    tdata = [go.Scatter(x = temp1.loc[temp1.continent ==i, 'gdpPercap'], 
                       y = temp1.loc[temp1.continent ==i, 'lifeExp'],
                       mode = 'markers', 
                       name = i,
                       marker = dict(size = 15),
                       opacity = 0.7
                      ) for i in temp1.continent.drop_duplicates()]
    tlayout = go.Layout(title = 'Class 2_08 Multiple Input', 
                       xaxis = dict(title = 'GDP Per Capitna'),
                       yaxis = dict(title = 'Life Expectancy'),
                       hovermode= 'closest')
    return dict(data = tdata, layout = tlayout)

@app.callback(Output(component_id = 'drop_class_2_09_sub2', component_property = 'options'),
              [Input(component_id = 'drop_class_2_09_sub1',component_property = 'value')])

def class_2_09(c209):
    new_option = [dict(label = i, value = i ) for i in df_2_09.columns if i != c209]
    return new_option

@app.callback(Output(component_id = 'class_2_09', component_property = 'figure'),
              [Input(component_id = 'drop_class_2_09_sub1',component_property = 'value'),
               Input(component_id = 'drop_class_2_09_sub2',component_property = 'value')],
              prevent_initial_call = True)

def class_2_09_final(t1, t2):
    data209 = [go.Scatter(x = df_2_09[t1],
                          y = df_2_09[t2],
                          mode ='markers', 
                          marker = dict(size = 10,
                                        opacity = 0.7))]
    layout209 = go.Layout(title = 'Class 2_09 Multiple outputs', 
                          xaxis = dict(title = f'{t1}'),
                          yaxis = dict(title = f'{t2}'))
    
    return dict(data= data209, layout = layout209)

@app.callback(Output(component_id = 'Slider_class_2_10', component_property = 'value'),
              [Input(component_id = 'Slider_class_2_10', component_property = 'value')])

def class_201(ck210):

    if ck210[0] == ck210[1]:
        return [ck210[0]-1, ck210[1]]
    else:
        return ck210

@app.callback(Output(component_id = 'class_2_10_result', component_property = 'children'),
              [Input(component_id = 'Slider_class_2_10', component_property = 'value')])

def class_210(c210):
    return c210[0] * c210[1]


@app.callback(Output(component_id = 'class_2_12_out', component_property = 'children'),
              [Input(component_id = 'class_2_12_button', component_property = 'n_clicks')],
              [State(component_id = 'class_2_12_input', component_property = 'value')])

def class_212(nt, c212):

    return f'{10 + int(c212)}'

@app.callback(Output(component_id = 'class_2_13_out', component_property = 'children'), 
              [Input(component_id = 'class_2_13', component_property = 'hoverData')])

def class_213(c213):
    return json.dumps(c213, indent = 2)

@app.callback(Output(component_id = 'class_2_13_img', component_property = 'src'),
              [Input(component_id = 'class_2_13', component_property = 'hoverData')])

def class_213_p2(c213_2):
    c213_x = df_2_13.wheels == c213_2['points'][0]['y']
    c213_y =  df_2_13.color == c213_2['points'][0]['x']
    return encode_image('data/Images/' + df_2_13.loc[c213_x & c213_y,].iloc[0,2])

if __name__ == '__main__':
    app.run()
