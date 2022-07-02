# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:20:41 2022

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

csk = pd.read_csv('csk(sql).csv')

app = dash.Dash(__name__)


app.layout = html.Div(children=[html.H1('CSK vs Opponents Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                
                                dcc.Dropdown(id='team-dropdown',
                                            options=[
                                                         {'label': 'ALL TEAMS', 'value': 'ALL'},
                                                         {'label': 'Mumbai Indians', 'value': 'Mumbai Indians'},
                                                         {'label': 'Rajasthan Royals', 'value': 'Rajasthan Royals'},
                                                         {'label': 'Punjab Kings', 'value': 'Punjab Kings'},
                                                         {'label': 'Delhi Capitals', 'value': 'Delhi Capitals'},
                                                         {'label': 'Royal Challengers Bangalore', 'value': 'Royal Challengers Bangalore'},
                                                         {'label': 'Sunrisers Hyderabad', 'value': 'Sunrisers Hyderabad'},
                                                         {'label': 'Kolkata Knight Riders', 'value': 'Kolkata Knight Riders'},
                                                         {'label': 'Pune Warriors', 'value': 'Pune Warriors'},
                                                         {'label': 'Kochi Tuskers Kerala', 'value': 'Kochi Tuskers Kerala'}
                                                    ],
                                            value='ALL',
                                            placeholder="Select a Team here", 
                                            searchable=True),
                                html.Br(),

                                html.Div(dcc.Graph(id='success-pie-chart')),
                               ])

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='team-dropdown', component_property='value'))

def build_graph(team_dropdown):
    if team_dropdown == 'ALL':
        piechart = px.pie(data_frame = csk, names='Opponent', values='csk' ,title='Total CSK Wins against All Teams', width = 650, height = 650)
        return piechart
    else:
        specific_df=csk.loc[csk['Opponent'] == team_dropdown]
        piechart = px.pie(data_frame = specific_df, names = 'csk', title='CSK performance against a Specific Team', width = 650, height = 650)
        return piechart

if __name__ == '__main__':
    app.run_server()