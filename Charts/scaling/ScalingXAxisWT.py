import os
from itertools import cycle

import dash
from dash import dcc
from dash import html
from dash import dash_table
from dash import Dash, Input, Output, callback
from jupyter_dash import JupyterDash
import dash_bootstrap_components as dbc

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define scale factors
def get_scale_factor(unit):
    BARN_CM2= 1e-24
    
    if (unit == "b"):
        return BARN_CM
    elif (unit == "mb"):
        return 1e-3*BARN_CM2
    elif (unit == "ub"):
        return 1e-6*BARN_CM2
    elif (unit == "nb"):
        return 1e-9*BARN_CM2
    elif (unit == "pb"):
        return 1e-12*BARN_CM2
    elif (unit == "fb"):
        return 1e-15*BARN_CM2
    elif (unit == "ab"):
        return 1e-18*BARN_CM2
    elif (unit == "zb"):
        return 1e-21*BARN_CM2
    elif (unit == "yb"):
        return 1e-24*BARN_CM2
    else: 
        return 1

cwd = os.getcwd()
COMPONENT_STYLE = "/assets/my_component.css"
external_stylesheets=[dbc.themes.BOOTSTRAP]

app = JupyterDash(__name__,requests_pathname_prefix="/dash1/",routes_pathname_prefix='/dash1/',
                  external_stylesheets=external_stylesheets,
                  meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}],
                 suppress_callback_exceptions=True)
# Create server variable with Flask server object for use with gunicorn
server = app.server
app.layout = html.Div(['Hello World'])

palette = cycle(px.colors.qualitative.Bold)

csv_df = pd.read_csv(cwd+'/data.csv')
data_df = csv_df

lol = []
for index, row in data_df.iterrows():
    #print(row['id'], row['data_values'])

    data_string = row[['data_values']].iloc[0]
    data_string = data_string.replace("{[", "")
    data_string = data_string.replace("]}", "")
    #print(data_string)
    data_series = data_string.split("]")
    #print(len(data_series))
    for l in range(0,len(data_series)):
        next_colour = next(palette)
        single_set = data_series[l]
        set_list = single_set.split(";")
        for i in set_list:
            z = i.split(" ");
            new_x = z[0].replace(",[", "")
            try:
                appendthis = [row['id'],l,new_x,z[1],next_colour]
            except:
                appendthis = [row['id'],l,0,0]
            lol.append(appendthis)
    #lol
df_experiment = pd.DataFrame(data=lol,columns=['experiment','series','raw_x','raw_y','series_color'])

unit = "zb" # this will probably be provided by the user via a drop-down menu
scale_factor = get_scale_factor(unit)

df_experiment['x'] = df_experiment['raw_x'].astype(str).astype(dtype = float, errors = 'ignore')

# add scale_factor here
df_experiment['y'] = df_experiment['raw_y'].astype(str).astype(dtype = float, errors = 'ignore')/scale_factor

df_plot = df_experiment
fig = px.scatter(df_plot, x='x', y='y', color='series')

fig.update_xaxes(type="log")
fig.update_yaxes(type="log")

fig.show()
