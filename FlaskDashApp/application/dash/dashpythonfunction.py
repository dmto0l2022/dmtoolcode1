import dash
from dash.dependencies import Input, Output
from dash import dash_table
from dash import html


def init_dashboard(server):
    app = dash.Dash(__name__)
    app.layout = html.Div([
        # ... Layout stuff
    ])

    # Initialize callbacks after our app is loaded
    # Pass dash_app as a parameter
    init_callbacks(dash_app)

    return dash_app.server


def init_callbacks(dash_app):
    @app.callback(
    # Callback input/output
    ....
    )
    def update_graph(rows):
        # Callback logic
        # ...
        
        
