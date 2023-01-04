#!/usr/bin/env python

import os

cwd = os.getcwd()
import flask
import dash
from dash import dcc
from dash import html
from dash import callback_context
from dash import dash_table

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dash import Dash, Input, Output, callback, State

import dash_bootstrap_components as dbc

import pandas as pd


import table_styling as ts
ts40 = ts.table40style
ts40.style_table_40
ts40.style_cell_9pt



#COMPONENT_STYLE = "/assets/my_component.css"
pages_styles = "/assets/pagestyles.css"
content_styles = "/assets/contents.css"
external_stylesheets=[dbc.themes.BOOTSTRAP, pages_styles, content_styles]


server = flask.Flask(__name__)
app = dash.Dash(__name__, use_pages=True,
                server=server,
                external_stylesheets=external_stylesheets,
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}],
                suppress_callback_exceptions=True)

from pages.sidebar import sidebar

import frame as frame
page_frame = frame.PageFrame()
page_frame.SetSideBarComponents(sidebar())
page_frame.PopulateFrame()



import plotly.graph_objects as go
import plotly.express as px
from itertools import cycle

# colors
palette = cycle(px.colors.qualitative.Bold)
#palette = cycle(['black', 'grey', 'red', 'blue'])


import plotly.graph_objects as go

fig1 = go.Figure()
fig2 = go.Figure()
fig3 = go.Figure()

fig1.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
))

fig2.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
))

fig3.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 2, 3, 4, 5, 6, 7, 8]
))


fig1.update_layout(
    autosize=True,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    paper_bgcolor="Green",
    xaxis_title="X AXIS TITLE",
    yaxis_title="Y AXIS TITLE",
)


#fig1.update_yaxes(automargin=True)
#fig1.update_xaxes(automargin=True)

fig2.update_layout(
    autosize=True,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    paper_bgcolor="Blue",
    xaxis_title="X AXIS TITLE",
    yaxis_title="Y AXIS TITLE",
)

#fig2.update_yaxes(automargin=True)
#fig2.update_xaxes(automargin=True)

fig3.update_layout(
    autosize=True,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=0
    ),
    paper_bgcolor="Blue",
    xaxis_title="X AXIS TITLE",
    yaxis_title="Y AXIS TITLE",
)

twographrows = [
    dbc.Row([
            dbc.Col([
                dcc.Graph(figure=fig1, id='basicgraph1', responsive=True, className="GRAPH CONTENT_NOPADDING")
            ])
            ], class_name="TOP_CHART_ROW CONTENT_NOPADDING"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=fig2, id='basicgraph2', responsive=True, className = "GRAPH CONTENT_NOPADDING")
            ])
        ], class_name = 'BOTTOM_CHART_ROW CONTENT_NOPADDING' ),
]

solar_df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')


dash_table1 = dash_table.DataTable(
            id='datatable1',
            data=solar_df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in solar_df.columns],
            fixed_rows={'headers': True},
            css=ts40.css_12pt, ## working
            style_table=ts40.style_table_40,
            style_cell=ts40.style_cell_9pt,
            )


dash_table2 = dash_table.DataTable(
            id='datatable2',
            data=solar_df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in solar_df.columns],
            fixed_rows={'headers': True},
            css=ts40.css_12pt, ## working
            style_table=ts40.style_table_40,
            style_cell=ts40.style_cell_9pt,
            )


dash_table3 = dash_table.DataTable(
            id='datatable3',
            data=solar_df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in solar_df.columns],
            fixed_rows={'headers': True},
            css=ts40.css_12pt, ## working
            style_table=ts40.style_table_40,
            style_cell=ts40.style_cell_9pt,
            )


twotablerows = [
    dbc.Row([dbc.Col(dash_table1)], class_name = "TABLE_ROW NOPADDING_CONTENT"),
    ##style={**TABLE_ROW,**NOPADDING}),
    dbc.Row([dbc.Col(dash_table2)], class_name = "TABLE_ROW NOPADDING_CONTENT")
    ##style={**TABLE_ROW,**NOPADDING}),
               ]

graphtablerow = [dbc.Row([
                dbc.Col([
                    dcc.Graph(figure=fig3,
                              id='basicgraph1',
                              responsive=True,
                              className = "GRAPH_STYLE NOPADDING_CONTENT",
                              #style={**GRAPH_STYLE,**NOPADDING}
                             )
                    ])
                ], class_name = "TOP_CHART_ROW NOPADDING_CONTENT"),
        dbc.Row([dbc.Col(dash_table3)],  className = "BOTTOM_TABLE_ROW NOPADDING_CONTENT"),
                 ]

column_1_var = 'Column 1'
column_2_var = twotablerows
column_3_var = graphtablerow

def GetThreeColumns(column_1_in, column_2_in, column_3_in):

    column_1_out =  html.Div(children=[column_1_in],
                                  className="col col-lg-2 NOPADDING_CONTENT COLUMN_DIV",
                            )
    
    column_2_out =  html.Div(children=column_2_in,
                                  className="col col-lg-5 NOPADDING_CONTENT COLUMN_DIV",
                                )
    
    column_3_out =  html.Div(children=column_3_in,
                                  className="col col-lg-5 NOPADDING_CONTENT COLUMN_DIV" ,
                            )
    
    threecolumnrow_out = dbc.Row([column_1_out,column_2_out, column_3_out],
                                 className="NOPADDING_CONTENT ALL_ROW")
    
    return threecolumnrow_out


threecolumnrow = GetThreeColumns(column_1_var, column_2_var, column_3_var) 


#content = [html.Div([
#    html.H1('Multi-page app with Dash Pages'),#
#
#    html.Div(
#        [
#            html.Div(
#                dcc.Link(
#                    f"{page['name']} - {page['path']}", href=page["relative_path"]
#                )
#            )
#            for page in dash.page_registry.values()
#        ]
#    ),
#    dash.page_container
#])]


#content = [html.Div([
#    html.H1('Multi-page app with Dash Pages'),
#    dash.page_container
#])]

#cdivs = [html.P("content", style=NOPADDING)]
#cdivs = [layout7]
cdivs = threecolumnrow
#cdivs = dash.page_container

content = [html.Div(cdivs,className = "PAGE_CONTENT PAGE_NOPADDING",)]

content_frame = page_frame.content_frame

full_layout = content_frame + content
#full_layout = content_frame

layout_empty = html.Div(full_layout,
                   className="container-fluid PAGE_PARENT_CONTAINER PAGE_NOPADDING",
                   #style={**PARENT_CONTAINER_STYLE,**NOPADDING},
                  )


chartrow = dbc.Row([
    dbc.Col([
        dcc.Graph(id='basicgraph', responsive=True, style={
            'display': 'block'
        })
    ])
], className="CONTENT_NOPADDING CHART_ROW",)

app.layout = layout_empty


#app.run_server(host="127.0.0.1", port=8002,debug=True)
app.run_server(debug=True,port=5050)


