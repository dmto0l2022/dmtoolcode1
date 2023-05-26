import dash
from dash import html, dcc

import formlibrary as fl

dash.register_page(__name__, path='/app/name_new_plot')

new_plot_row = fl.create_new_plot_form

layout = new_plot_row
