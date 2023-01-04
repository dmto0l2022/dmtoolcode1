import dash
from dash import html, dcc
import forms.formlibrary as fl

dash.register_page(__name__)

#layout = html.Div(children=[
#    html.H1(children='This is our Second page'),
#
#    html.Div(children='''
#        This is our Second page content.
#    '''),
#
#])

#layout = fl.newplot_input2

layout = fl.newplotform
