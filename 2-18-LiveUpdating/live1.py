import numpy as np 
import pandas as pd 
import plotly.express as px 
import plotly.graph_objects as go 
import plotly.offline as pyo
import plotly.figure_factory as ff
import dash 
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import json
import base64
import datetime as dt
import pandas_datareader.data as web

l2 = dash.Dash()

l2.layout = html.Div(
    [html.H1(id = 'Hello_world'),
    dcc.Interval(
        id = 'inter1',
        interval= 2000, # that is eq to 2 sec
        n_intervals= 0
    )]
)

@l2.callback(Output(component_id= 'Hello_world', component_property= 'children'),
            [Input(component_id= 'inter1', component_property= 'n_intervals')])

def updates_h(v1):
    return f"I have update {v1} times"

l2.run()