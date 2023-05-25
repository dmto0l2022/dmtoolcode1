import dash
from dash import html, dcc

import formlibrary as fl

dash.register_page(__name__, path='/app/select_limits_to_plot')

newplot_row = fl.newplot_form

layout = newplot_row
