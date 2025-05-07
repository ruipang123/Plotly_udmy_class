import pandas as pd 
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.figure_factory as ff
import dash
from dash import dcc, html

sec = dash.Dash()

color_map = {
    'backgroud': '#111111',
    'text': '#7FDBFF'
}

sec.layout = html.Div( children= [
    html.H1(
        children = 'New hello',
        style = {
            'textAlign': 'center',
            'color': color_map['text']
        }
    ),
    html.Div(
        children= 'Dash: A web application framework for python',
        style = {
            'textAlign': 'center',
            'color': color_map['text']
        }
    ),
    dcc.Graph(
            id = 'example-graph',
            figure = {
                'data':[
                    {'x': [1,2,3], 'y': [4,1,2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1,2,3], 'y': [2,4,5], 'type': 'bar', 'name': 'AG'}
                ],
                'layout':{
                    'plot_bgcolor': color_map['backgroud'],
                    'paper_bgcolor': color_map['backgroud'],
                    'font': dict(color = color_map['text']),
                    'title': 'Dash board first 1'
                }
            }
        )
    
], style= dict(backgroundColor = color_map['backgroud'])

)


if __name__ == "__main__":
        sec.run(debug=True, port=8051)