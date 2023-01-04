import dash
from dash import html, dcc

dash.register_page(__name__, path='/dash1/landing/')

layout = html.Div(children=[
    html.H1(children='This is our Landing page'),

    html.Div(children='''
        This is our Landing page content.
    '''),

])