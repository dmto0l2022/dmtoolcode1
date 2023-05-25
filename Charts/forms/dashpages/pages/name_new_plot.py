import dash
from dash import html, dcc

import formlibrary as fl

dash.register_page(__name__, path='/app/name_new_plot')

newplot_row = fl.newplot_form

layout = newplot_row
