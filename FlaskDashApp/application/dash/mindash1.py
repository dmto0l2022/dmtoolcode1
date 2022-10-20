import dash
from dash.dependencies import Input, Output
from dash import dcc
from dash import html

import flask
import pandas as pd
import time
import os

def init_callbacks(dash_app, df_in):
    @dash_app.callback(Output('my-graph', 'figure'),
                  [Input('my-dropdown', 'value')])
    def update_graph(selected_dropdown_value):
        dff = df_in[df_in['Stock'] == selected_dropdown_value]
        return {
            'data': [{
                'x': dff.Date,
                'y': dff.Close,
                'line': {
                    'width': 3,
                    'shape': 'spline'
                }
            }],
            'layout': {
                'margin': {
                    'l': 30,
                    'r': 20,
                    'b': 30,
                    't': 20
                }
            }
        }

def init_dashboard_functions(server):
    """Create a Plotly Dash dashboard."""

    # Create Dash Layout
    #dash_app.layout = html.Div(id='dash-container')

    server = flask.Flask('app')
    server.secret_key = "1234567890" # os.environ.get('secret_key', 'secret')

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/hello-world-stock.csv')

    
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=[
            '/static/styles.css',
        ]
    )

    dash_app.scripts.config.serve_locally = False
    dcc._js_dist[0]['external_url'] = 'https://cdn.plot.ly/plotly-basic-latest.min.js'

    dash_app.layout = html.Div([
        html.H1('Stock Tickers'),
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'},
                {'label': 'Coke', 'value': 'COKE'}
            ],
            value='TSLA'
        ),
        dcc.Graph(id='my-graph')
    ], className="container")
    
    init_callbacks(dash_app, df)
    
    return dash_app.server
