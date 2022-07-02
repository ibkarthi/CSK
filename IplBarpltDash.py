# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:48:48 2022

@author: ibd
"""

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import numpy as np

pitch = pd.read_csv('pitchwin.csv')
teams = pd.read_csv('OppTeam.csv')
days = pd.read_csv('MatchDay.csv')

app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('CSK Performance Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                
                                dcc.Dropdown(id='features-dropdown',
                                            options=[
                                                         {'label': 'Ground', 'value': 'Ground'},
                                                         {'label': 'Opponent', 'value': 'Opponent'},
                                                         {'label': 'Day', 'value': 'Day'}  
                                                    ],
                                            value='Ground',
                                            placeholder="Select a feature here", 
                                            searchable=True),
                                html.Br(),

                                html.Div(dcc.Graph(id='performance-bar-chart')),
                               ])

@app.callback(
    Output(component_id='performance-bar-chart', component_property='figure'),
    Input(component_id='features-dropdown', component_property='value'))

def build_graph(features_dropdown):
    if features_dropdown == 'Ground':
        bar = px.bar(pitch, x='Ground', y=['Cskplayed', 'Cskwon'], title='CSKs Performance in all grounds', barmode = 'overlay')
        #bar2 = px.bar(pitch, x='Ground', y='Cskwon')
        return bar
    
    elif features_dropdown == 'Opponent':
        bar = px.bar(teams, x='Opponent', y=['CSKPlayed', 'CSKWon'], title='CSKs Performance against all teams', barmode = 'overlay')
        #bar2 = px.bar(teams, x='Opponent', y='CSKWon')
        return bar
    
    else:
        bar = px.bar(days, x='Day', y=['Cskplayed', 'Cskwon'], title='CSKs Performance in all days', barmode = 'overlay')
        #bar2 = px.bar(days, x='Day', y='Cskwon')
        return bar

if __name__ == '__main__':
    app.run_server(port = '8050')