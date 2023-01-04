#!/usr/bin/env python
# coding: utf-8

# In[1]:


#!pip install dash_bootstrap_components


# In[2]:


import os


# In[3]:


cwd = os.getcwd()


# In[4]:


import dash
from dash import dcc
from dash import html
from dash import callback_context
from dash import dash_table

import plotly.graph_objects as go
from plotly.subplots import make_subplots

from dash import Dash, Input, Output, callback, State

from jupyter_dash import JupyterDash

import dash_bootstrap_components as dbc


# In[5]:


import pandas as pd


# In[6]:


import table_styling as ts
ts40 = ts.table40style
ts40.style_table_40
ts40.style_cell_9pt


# In[7]:


from pages.sidebar import sidebar


# In[8]:


#COMPONENT_STYLE = "/assets/my_component.css"
pages_styles = "/assets/pagestyles.css"
content_styles = "/assets/contents.css"
external_stylesheets=[dbc.themes.BOOTSTRAP, pages_styles, content_styles]


# In[9]:


app = JupyterDash(__name__,
                  use_pages=True,
                  #requests_pathname_prefix="/dash1/",
                  #routes_pathname_prefix='/dash1/',
                  external_stylesheets=external_stylesheets,
                  meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}],
                 suppress_callback_exceptions=True)
# Create server variable with Flask server object for use with gunicorn
server = app.server


# In[ ]:


import frame as frame
page_frame = frame.PageFrame()


# In[ ]:


page_frame.content_frame


# In[ ]:


sidebar()


# In[ ]:


page_frame.SetSideBarComponents(sidebar())


# In[ ]:


page_frame.PopulateFrame()


# # Color Code

# In[ ]:


import plotly.graph_objects as go
import plotly.express as px
from itertools import cycle

# colors
palette = cycle(px.colors.qualitative.Bold)
#palette = cycle(['black', 'grey', 'red', 'blue'])


# In[ ]:


#pf = pageframe()


# In[ ]:


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


# In[ ]:


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


# In[ ]:


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

#dash_table1


# In[ ]:


dash_table2 = dash_table.DataTable(
            id='datatable2',
            data=solar_df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in solar_df.columns],
            fixed_rows={'headers': True},
            css=ts40.css_12pt, ## working
            style_table=ts40.style_table_40,
            style_cell=ts40.style_cell_9pt,
            )


# In[ ]:


dash_table3 = dash_table.DataTable(
            id='datatable3',
            data=solar_df.to_dict('records'),
            columns=[{"name": i, "id": i} for i in solar_df.columns],
            fixed_rows={'headers': True},
            css=ts40.css_12pt, ## working
            style_table=ts40.style_table_40,
            style_cell=ts40.style_cell_9pt,
            )


# In[ ]:


twotablerows = [
    dbc.Row([dbc.Col(dash_table1)], class_name = "TABLE_ROW NOPADDING_CONTENT"),
    ##style={**TABLE_ROW,**NOPADDING}),
    dbc.Row([dbc.Col(dash_table2)], class_name = "TABLE_ROW NOPADDING_CONTENT")
    ##style={**TABLE_ROW,**NOPADDING}),
               ]


# In[ ]:


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


# In[ ]:


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

header = html.Div([
    html.P('Dashboard Template')], className = "PAGE_HEADER" , #style={**HEADER_STYLE,**NOPADDING},
)

fdivs = [html.P("ACG / WT")]
footer = html.Div(fdivs, className = "PAGE_FOOTER PAGE_NOPADDING",) #style={**FOOTER_STYLE,**NOPADDING},)



#legend_out_graph
#footer = html.Div(fdivs, style=FOOTER_STYLE,)
#footer = html.Div(filters, style=FOOTER_STYLE,)

adbar = html.Div([
    html.P('R')],
    className = "PAGE_ADBAR PAGE_NOPADDING"
    #style={**ADBAR_STYLE,**NOPADDING},
)

sidebar = html.Div(
    [html.P("L", className="lead")],
    #filters,
    className = "PAGE_SIDEBAR PAGE_NOPADDING",
    #style={**SIDEBAR_STYLE,**NOPADDING},
)

# In[10]:


headertext = "Dark Matter Tool"
footertext = "ACG"

def GetHeaderAndFooter(headertext, footertext):


    hdivs = html.P(headertext)
    header1 = html.Div([hdivs], className = "FULL_DIV PAGE_NOPADDING",)

    fdivs = [html.P(footertext)]
    
    footer1 = html.Div(fdivs, className = "FULL_DIV PAGE_NOPADDING",)

    #headerrow_out =  html.Div(children=[header1],className = "row PAGE_HEADER PAGE_NOPADDING",)

    #footerrow_out =  html.Div(children=[footer1],className = "row PAGE_FOOTER PAGE_NOPADDING",)
    
    header_out =  html.Div(children=[header1],className = "PAGE_HEADER PAGE_NOPADDING",)

    footer_out =  html.Div(children=[footer1],className = "PAGE_FOOTER PAGE_NOPADDING",)
    
    return header_out, footer_out

page_header, page_footer = GetHeaderAndFooter(headertext, footertext)


# In[11]:


l_sidebar_in = 'L sidebar'
r_sidebar_in = 'R sidebar'

def GetSideBars(l_sidebar_in, r_sidebar_in):

    l_sidebar_out =  html.Div(children='L sidebar',
                                  className="PAGE_NOPADDING PAGE_SIDE_LEFT",)
    
    r_sidebar_out =  html.Div(children='R sidebar',
                                  className="PAGE_NOPADDING PAGE_SIDE_RIGHT",)
    
    
    return l_sidebar_out, r_sidebar_out


page_l_sidebar, page_r_sidebar = GetSideBars(l_sidebar_in, r_sidebar_in) 


# In[12]:


page_l_sidebar


# In[13]:


#content_frame = page_frame.content_frame
#content_frame

content = [html.Div([
    html.H1('Multi-page app with Dash Pages'),

    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ]
    ),
    dash.page_container
])]content = [html.Div([
    html.H1('Multi-page app with Dash Pages'),
    dash.page_container
])]
# In[ ]:




#cdivs = [html.P("content", style=NOPADDING)]
#cdivs = [layout7]
#cdivs = threecolumnrow
cdivs = dash.page_container

content = [html.Div(cdivs,className = "PAGE_CONTENT PAGE_NOPADDING",)]

#content_frame = [page_header,page_l_sidebar,page_r_sidebar,page_footer]
#content_frame = [page_l_sidebar,page_r_sidebar]

#content_frame = [page_header,page_footer]



full_layout = content_frame + content
#full_layout = content_frame

layout_empty = html.Div(full_layout,
                   className="container-fluid PAGE_PARENT_CONTAINER PAGE_NOPADDING",
                   #style={**PARENT_CONTAINER_STYLE,**NOPADDING},
                  )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


maincolumn = dbc.Col(
            [
               html.P('Main Column')
            ],
            width=10,)


# In[ ]:


chartrow = dbc.Row([
    dbc.Col([
        dcc.Graph(id='basicgraph', responsive=True, style={
            'display': 'block'
        })
    ])
], className="CONTENT_NOPADDING CHART_ROW",)

charttwotablecolumn = dbc.Col(
            [
                chartrow,row3_1,row3_2
            ],
            width=10,)fourcolumns =  html.Div(className="row ALL_ROW CONTENT_NOPADDING",
                        children=[l_sidebar_col,##column_chart,
                                                  maincolumn,
                                                  r_sidebar_col,],
                       )

layout4 = html.Div([headerrow,fourcolumns,footerrow],
                   className="container-fluid PAGE_PARENT_CONTAINER",
                  )

#app.layout = layout4
# In[ ]:


app.layout = layout_empty

https://dash.plotly.com/datatable/interactivity
# In[ ]:


#app.run_server(host="127.0.0.1", port=8002,debug=True)
app.run_server(debug=True,port=5050)


# {'report_name': 'report_name', 'ad_account': 'ad_account', 'app_id': 'app_id', 'access_token': 'access_token1'}
