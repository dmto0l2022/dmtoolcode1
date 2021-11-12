import dash

from jupyter_dash import JupyterDash

import dash_bootstrap_components as dbc
COMPONENT_STYLE = "/assets/my_component.css"
external_stylesheets=[dbc.themes.BOOTSTRAP]

app = JupyterDash(__name__, external_stylesheets=external_stylesheets,
                  meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}],
                 suppress_callback_exceptions=True)

server = app.server