import dash
from dash import html, dcc

dash.register_page(__name__, path='/app/home1')

layout = html.Div(children=[
    html.H1(children='This is our Home page'),

    html.Div(children='''
        This is our Home page content.
    '''),

])
