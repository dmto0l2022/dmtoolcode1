import dash
from dash import html, dcc

import formlibrary as fl

dash.register_page(__name__, path='/app/edit_existing_limit')

edit_existing_limit_row = fl.edit_existing_limit_form

layout = edit_existing_limit_row
