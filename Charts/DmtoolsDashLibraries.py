import pandas as pd

import dash
from dash import dcc
from dash import html
from dash import dash_table

import plotly.graph_objects as go
import plotly.express as px
from itertools import cycle

from plotly.subplots import make_subplots

# colors
palette = cycle(px.colors.qualitative.Bold)
#palette = cycle(['black', 'grey', 'red', 'blue'])

# Define scale factors [WT]
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
    

    
def datastring2dataframe(row_in):
    #try:
    #data_list = row_in['data_values'].tolist()
    #data_list = row[['data_values']].iloc[0]
    #if isinstance(data_list, pd.DataFrame):
    #    row_data = next(data_list.iterrows())[1]
    #else:
    #    row_data = data_list
    data_string = row_in[['data_values']].iloc[0]
    data_string = data_string.replace("{[", "")
    data_string = data_string.replace("]}", "")
    x = data_string.split(";")
    lol = []
    
    
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
                appendthis = [row_in['id'],row_in['data_label'],l,new_x,z[1],next_colour]
            except:
                appendthis = [row_in['id'],l,0,0]
            lol.append(appendthis)
    
    #for i in x:
    #    z = i.split(" ");
    #    appendthis = [z[0],z[1]]
    #    lol.append(appendthis)
    #lol
    df_experiment = pd.DataFrame(data=lol,columns=['id','data_label','series','raw_x','raw_y','suggested_color'])

    unit = "zb" # this will probably be provided by the user via a drop-down menu
    scale_factor = float(get_scale_factor(unit))


    df_experiment['x'] = df_experiment['raw_x'].astype(str).astype(dtype = float, errors = 'ignore')

    # add scale_factor here
    df_experiment['y'] = df_experiment['raw_y'].astype(str).astype(dtype = float, errors = 'ignore')#/scale_factor
    #df_experiment['y'] =  df_experiment['y'].div(scale_factor).round(2)
    df_experiment['scale_factor'] = scale_factor
    df_experiment['scaled_y'] = \
    df_experiment[['y','scale_factor']].apply(pd.to_numeric,errors='coerce').fillna(0).eval('y/scale_factor')
    #'experiment',
    #'series'
    
    #except:
    #    data_null = [[0,0]]
    #    df_experiment = pd.DataFrame(data=data_null,columns=['raw_x','raw_y'])#

    #    df_experiment['x'] = df_experiment['raw_x'].astype(str).astype(float)
    #    df_experiment['y'] = df_experiment['raw_y'].astype(str).astype(float)
    #df_experiment.dtypes
    return df_experiment


def CreatePlotSeries(limits_df_in, result_ids_in):
    
    multiresult_df = limits_df_in[limits_df_in['id'].isin(result_ids_in)]

    data_df = multiresult_df

    lol = []
    df_experiment_all_out=pd.DataFrame()
    for index, row in data_df.iterrows():
        df_experiment_one =  datastring2dataframe(row)
        if df_experiment_all_out.empty:
            df_experiment_all_out = df_experiment_one
        else:
            df_experiment_all_out = pd.concat([df_experiment_all_out, df_experiment_one])


    plotseries_out = df_experiment_all_out[['id','data_label','series','suggested_color']]
    plotseries_out = plotseries_out.drop_duplicates()
    plotseries_out = plotseries_out.reset_index(drop=True)
    plotseries_out['color'] = 'black'
    plotseries_out['line'] = 'solid'
    plotseries_out['symbol'] = 'square'
    
    return plotseries_out, df_experiment_all_out


#result_ids = [1,2]
#plotseries, df_experiment_all = CreatePlotSeries(result_ids_in)

def CreateDefaultFormatTable(plotseries_in):

    color_list = ['black','red','orange','yellow','lime green', 'green', 'blue-green', 'cyan',
              'sky blue', 'blue', 'purple', 'magenta', 'pink']

    color_options=[{'label': i, 'value': i} for i in color_list]
    
    line_styles_list = ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
    
    line_styles_options=[{'label': i, 'value': i} for i in line_styles_list]
    
    symbol_list = ['circle','square','diamond','cross','x','hexagon','pentagon','octagon','star','asterisk','hash']
    
    symbol_options=[{'label': i, 'value': i} for i in symbol_list]
    
    format_table_div_out = html.Div([
        dash_table.DataTable(
            id='format_table_id',
            #row_deletable=True,
            # Add this line
            data=plotseries_in.to_dict('records'),
            columns=[
                {'id': 'id', 'name': 'id'},
                {'id': 'data_label', 'name': 'data_label'},
                {'id': 'series', 'name': 'series'},
                {'id': 'color', 'name': 'color', 'presentation': 'dropdown'},
                {'id': 'line', 'name': 'line', 'presentation': 'dropdown'},
                {'id': 'symbol', 'name': 'symbol', 'presentation': 'dropdown'},
            ],

            editable=True,
            css=[
                {"selector": ".Select-menu-outer", "rule": "display: block !important"},
                {"selector": ".dash-spreadsheet tr th", "rule": "height: 5px;"},  # set height of header
                {"selector": ".dash-spreadsheet tr td", "rule": "height: 5px;"}  # set height of body rows
                ],

            dropdown={
                'color': {
                    'options': [
                        {'label': i, 'value': i}
                        for i in color_list
                    ]
                },
                'line': {
                     'options': [
                        {'label': i, 'value': i}
                        for i in line_styles_list
                    ]
                },
                'symbol': {
                     'options': [
                        {'label': i, 'value': i}
                        for i in symbol_list
                    ]
                }
            },
            style_cell={'fontSize':12, 'font-family':'sans-serif', 'padding':'0px'},
            style_cell_conditional=[
                {'if': {'column_id': 'id'},
                 'width': '5%'},
                {'if': {'column_id': 'data_label'},
                 'width': '70%'},
                {'if': {'column_id': 'series'},
                 'width': '5%'},
                {'if': {'column_id': 'color'},
                 'width': '5%'},
                {'if': {'column_id': 'lime'},
                 'width': '5%'},
                 {'if': {'column_id': 'color'},
                 'width': '5%'},
                {'if': {'column_id': 'symbol'},
                 'width': '5%'}],
        ),
        html.Div(id='table-dropdown-container')
    ])

    return format_table_div_out

#table = CreateDefaultFormatTable(plotseries)
def CreateLegendFig(plotseries_in):
    
    rows_list = list(range(1,6))
    cols_list = list(range(1,6))
    
    table_rows=12
    table_cols=5
    
    fig_legend_out = make_subplots(
    column_titles = ['id','series','result','line', 'symbol'],
    rows=table_rows,
    cols=table_cols,
    horizontal_spacing = 0.00,
    vertical_spacing = 0.00,
    #subplot_titles=(titles)
    column_widths=[0.1,0.1,0.6,0.1, 0.1],)
    
    
    #fig_legend_out.update_xaxes(matches=None, showticklabels=True)
    #fig_legend_out.update_yaxes(matches=None, showticklabels=True)
    
    #fig_legend_out.update_layout(xaxis_range=[1,2])

    
    fig_legend_out.update_layout(
        autosize=False,
        width=800,
        height=200,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=20,
            pad=0
        ),
        #paper_bgcolor="LightSteelBlue",
    )
    
    rowloop = 0

    for index, row in plotseries_in.iterrows():
        #print(row['c1'], row['c2'])
        rowloop +=1
        for c in cols_list: #enumerate here to get access to i
            # STEP 2, notice position of arguments!
            table_column_names = ['id','series','data_label','line','symbol']
            scatter_mode_list = ['text-number','text-number','text-text','lines','markers']
            current_column = table_column_names[c-1]
            current_mode = scatter_mode_list[c-1]
            if current_mode =='lines':
                fig_legend_out.add_trace(go.Scatter(x=[1,2],
                                         y=[1,1],
                                         mode=current_mode,
                                         #text=row[current_column],
                                         line=dict(width=4,dash=row['line'],color=row['color']),
                                        ),
                              row=rowloop, #index for the subplot, i+1 because plotly starts with 1
                              col=c)
            if current_mode =='text-text':
                fig_legend_out.add_trace(go.Scatter(x=[1,2], 
                                         textposition='middle right',
                                         y=[1,1],
                                         mode='text',
                                         text=[row[current_column],'']
                                        ),
                              row=rowloop, #index for the subplot, i+1 because plotly starts with 1
                              col=c)
            
            if current_mode =='text-number':
                fig_legend_out.add_trace(go.Scatter(x=[1], 
                                         textposition='middle right',
                                         y=[1],
                                         mode='text',
                                         text=row[current_column]
                                        ),
                              row=rowloop, #index for the subplot, i+1 because plotly starts with 1
                              col=c)
            if current_mode =='markers':
                fig_legend_out.add_trace(go.Scatter(x=[1], 
                                        y=[1],
                                        mode=current_mode,
                                        #text=row[current_column],
                                        marker_symbol=row['symbol'],
                                        marker=dict(
                                        size=10,
                                        color=row['color'],#set color equal to a variable
                                        colorscale='Viridis', # one of plotly colorscales
                                        showscale=False,
                                        )
                                        ),
                              row=rowloop, #index for the subplot, i+1 because plotly starts with 1
                              col=c)
                
            fig_legend_out.update_xaxes(showgrid=False)
            fig_legend_out.update_yaxes(showgrid=False)
            #legend
            fig_legend_out.update_layout(showlegend=False)
            #x axis
            fig_legend_out.update_xaxes(visible=False)
            #y axis    
            fig_legend_out.update_yaxes(visible=False)

    return fig_legend_out

#fig_legend = CreateLegendFig(plotseries_default)
#fig_legend
def UpdateGraph(limits_df_in,plotseries_in):
    #result_ids = [1,262]
    result_ids_plot = plotseries_in['id'].unique().tolist()
    
    plotseries_default, df_experiment_plot = CreatePlotSeries(limits_df_in, result_ids_plot)
    #plotseries_default_plot = CreatePlotSeriesDefault(df_experiment_all_plot)

        # Create figure
    fig3 = go.Figure()

    for index, row in plotseries_in.iterrows():
        trace_data = df_experiment_plot[(df_experiment_plot['id']==row['id']) & (df_experiment_plot['series']==row['series'])]

    
        trace2add = trace_data

        trace_name = str(row['id']) + str(row['series'])
        
        fig3.add_trace(go.Scatter(x=trace2add['x'], y=trace2add['scaled_y'],
                            mode='lines+markers', # 'lines' or 'markers'
                            line=dict(width=4,dash=row['line'],color=row['color']),
                            #showscale=False,
                            marker_symbol=row['symbol'],
                                 marker=dict(
                                size=10,
                                color=row['color'],#set color equal to a variable
                                #colorscale='Viridis', # one of plotly colorscales
                                showscale=False,
                            ),
                            legendgroup=str(row['id']),  # this can be any string, not just "group"
                            legendgrouptitle_text=str(row['id']),
                            name=str(row['series'])
                                 ))

        #fig3.add_trace(go.Scatter(x=trace2add['x'], y=trace2add['scaled_y'],
        #                   mode='markers', # 'lines' or 'markers'
        #                    marker_symbol=row['symbol'],
        #                         marker=dict(
        #                        size=10,
        #                        color=row['color'],#set color equal to a variable
        #                        #colorscale='Viridis', # one of plotly colorscales
        #                        showscale=False,
        #                    ),
        #                    name=str(row['id'])))

    return fig3
#result_ids = [1,262]
#fig5 = UpdateGraph(plotseries_default)
#fig5.show()
def diff_dashtable(data, data_previous, row_id_name="id"):

    """Generate a diff of Dash DataTable data.

    Parameters
    ----------
    data: DataTable property (https://dash.plot.ly/datatable/reference)
        The contents of the table (list of dicts)
    data_previous: DataTable property
        The previous state of `data` (list of dicts).

    Returns
    -------
    A list of dictionaries in form of [{row_id_name:, column_name:, current_value:,
        previous_value:}]
    """

    df, df_previous = pd.DataFrame(data=data), pd.DataFrame(data_previous)

    for _df in [df, df_previous]:

        assert row_id_name in _df.columns

        _df = _df.set_index(row_id_name)

    mask = df.ne(df_previous)

    df_diff = df[mask].dropna(how="all", axis="columns").dropna(how="all", axis="rows")

    changes = []

    for idx, row in df_diff.iterrows():

        row_id = row.name

        row.dropna(inplace=True)

        for change in row.iteritems():

            changes.append(
                {
                    row_id_name: row_id,
                    "column_name": change[0],
                    "current_value": change[1],
                    "previous_value": df_previous.at[row_id, change[0]],
                }
            )

    return changes
