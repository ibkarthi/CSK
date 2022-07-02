# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:48:32 2022

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

app.layout = html.Div(children=[html.H1('CSK Match Days Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                
                                dcc.Dropdown(id='days-dropdown',
                                            options=[
                                                         {'label': 'ALL DAYS', 'value': 'ALL'},
                                                         {'label': 'Saturday', 'value': 'Saturday'},
                                                         {'label': 'Sunday', 'value': 'Sunday'},
                                                         {'label': 'Wednesday', 'value': 'Wednesday'},
                                                         {'label': 'Tuesday', 'value': 'Tuesday'},
                                                         {'label': 'Thursday', 'value': 'Thursday'},
                                                         {'label': 'Friday', 'value': 'Friday'},
                                                         {'label': 'Monday', 'value': 'Monday'}
                                                    ],
                                            value='ALL',
                                            placeholder="Select a Day here", 
                                            searchable=True),
                                html.Br(),

                                html.Div(dcc.Graph(id='success-pie-chart')),
                               ])

@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='days-dropdown', component_property='value'))

def build_graph(days_dropdown):
    if days_dropdown == 'ALL':
        piechart = px.pie(data_frame = csk, names='Day', values='csk', title='Total CSK matches for All Days')
        #piechart = plt.pie(days['Win%'], labels = days['Day'], colors=palette_color, autopct='%.2f%%')
        return piechart
    else:
        specific_df=csk.loc[csk['Day'] == days_dropdown]
        piechart = px.pie(data_frame = specific_df, names = 'csk', title='CSK performance for a Specific Day')
        #piechart = plt.pie([specific_df['Win%'], specific_df['Lose%']], labels = ['Win', 'Lose'], colors=palette_color, autopct='%.2f%%')
        return piechart

if __name__ == '__main__':
    app.run_server()