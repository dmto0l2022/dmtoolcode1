import dash
from dash import html, dcc

import formlibrary as fl

dash.register_page(__name__, path='/app/edit_existing_plot')

edit_existing_plot_row = fl.edit_existing_plot_form

layout = edit_existing_plot_row
