from dash import html

import dash
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    name="Topics",
    top_nav=True,
)


def layout():
    return dbc.Row(
        [dbc.Col(html.Div("Topics Home Page"), width=10)]
    )
