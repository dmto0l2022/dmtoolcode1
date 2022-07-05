from dash import html

layout = html.Div([
    html.Button('Click me', id='btn'),
    html.Div(id='output')
])
