import dash
from dash import html, dcc

import formlibrary as fl

dash.register_page(__name__, path='/app/create_new_limit')

new_limit_row = fl.create_new_limit_form

layout = new_limit_row
