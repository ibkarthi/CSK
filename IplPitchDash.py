# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:06:46 2022

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


app.layout = html.Div(children=[html.H1('CSK Pitch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                
                                dcc.Dropdown(id='pitch-dropdown',
                                            options=[
                                                         {'label': 'ALL SITES', 'value': 'ALL'},
                                                         {'label': 'Chennai', 'value': 'Chennai'},
                                                         {'label': 'Mumbai', 'value': 'Mumbai'},
                                                         {'label': 'Dubai', 'value': 'Dubai'},
                                                         {'label': 'Kolkata', 'value': 'Kolkata'},
                                                         {'label': 'Delhi', 'value': 'Delhi'},
                                                         {'label': 'Bengaluru', 'value': 'Bengaluru'},
                                                         {'label': 'Pune', 'value': 'Pune'},
                                                         {'label': 'Abu Dhabi', 'value': 'Abu Dhabi'},
                                                         {'label': 'Sharjah', 'value': 'Sharjah'},
                                                         {'label': 'Mohali', 'value': 'Mohali'},
                                                         {'label': 'Jaipur', 'value': 'Jaipur'},
                                                         {'label': 'Hyderabad', 'value': 'Hyderabad'},
                                                         {'label': 'Ranchi', 'value': 'Ranchi'},
                                                         {'label': 'Durban', 'value': 'Durban'},
                                                         {'label': 'Visakhapatnam', 'value': 'Visakhapatnam'},
                                                         {'label': 'Port Elizabeth', 'value': 'Port Elizabeth'},
                                                         {'label': 'Johannesburg', 'value': 'Johannesburg'},
                                                         {'label': 'East London', 'value': 'East London'},
                                                         {'label': 'Dharamsala', 'value': 'Dharamsala'},
                                                         {'label': 'Centurion', 'value': 'Centurion'},
                                                         {'label': 'Ahmedabad', 'value': 'Ahmedabad'},
                                                         {'label': 'Raipur', 'value': 'Raipur'},
                                                         {'label': 'Nagpur', 'value': 'Nagpur'},
                                                         {'label': 'Kochi', 'value': 'Kochi'},
                                                         {'label': 'Kimberley', 'value': 'Kimberley'},
                                                         {'label': 'Cuttack', 'value': 'Cuttack'},
                                                         {'label': 'Cape Town', 'value': 'Cape Town'}
                                                    ],
                                            value='ALL',
                                            placeholder="Select a Pitch here", 
                                            searchable=True),
                                html.Br(),

                                html.Div(dcc.Graph(id='success-pie-chart')),
                               ])

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='pitch-dropdown', component_property='value'))

def build_graph(pitch_dropdown):
    if pitch_dropdown == 'ALL':
        piechart = px.pie(data_frame = csk, names='Ground', values='csk' ,title='Total CSK Wins for All Pitches', width = 650, height = 650)
        return piechart
    else:
        specific_df=csk.loc[csk['Ground'] == pitch_dropdown]
        piechart = px.pie(data_frame = specific_df, names = 'csk', title='CSK performance for a Specific Pitch', width = 650, height = 650)
        return piechart

if __name__ == '__main__':
    app.run_server()