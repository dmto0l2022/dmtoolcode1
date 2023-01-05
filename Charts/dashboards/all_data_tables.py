from sqlalchemy import create_engine
import pandas as pd
from dash import dash_table

import os
from os import environ, path

from dotenv import load_dotenv

load_dotenv(".env")

import mariadb

MARIADB_USERNAME = environ.get("MARIADB_USERNAME")
MARIADB_PASSWORD = environ.get("MARIADB_PASSWORD")
#MARIADB_DATABASE = environ.get("MARIADB_DATABASE")
MARIADB_DATABASE = 'data'
MARIADB_CONTAINER = environ.get("MARIADB_CONTAINER")

MARIADB_URI = "mariadb+mariadbconnector://" + MARIADB_USERNAME + ":" + \
                    MARIADB_PASSWORD + "@" + MARIADB_CONTAINER + ":3306/"\
                    + MARIADB_DATABASE

#import psycopg2
engine = create_engine(MARIADB_URI)

##sqlquery = '''SELECT id, name FROM RubyDB.experiments;'''

experiments_sql = '''select distinct experiment as label, experiment as value 
FROM RubyDB.limits;'''

experiments_df = pd.read_sql_query(experiments_sql, engine)

result_types_sql = '''SELECT distinct
case
when result_type = "Th" then "Theory"
when result_type = "Proj" then "Project"
when result_type = "Exp" then "Experiment"
else result_type end label,
result_type as value
FROM RubyDB.limits;'''

result_types_df = pd.read_sql_query(result_types_sql, engine)

spin_dependency_sql = '''SELECT distinct
case
when spin_dependency = 'SD' then 'spin-dependent'
when spin_dependency = 'SI' then 'spin-indpendent'
else spin_dependency end label,
spin_dependency as value
FROM RubyDB.limits;'''

spin_dependency_df = pd.read_sql_query(spin_dependency_sql, engine)

greatest_hit_sql = '''select distinct
case
when greatest_hit = 0 then 'No'
when greatest_hit = 1 then 'Yes'
else greatest_hit end label,
 greatest_hit value
FROM RubyDB.limits;'''

greatest_hit_df = pd.read_sql_query(greatest_hit_sql, engine)

limits_sql = '''SELECT
id, spin_dependency, result_type, measurement_type, nomhash, x_units, y_units, x_rescale,
y_rescale, default_color, default_style,
data_values, data_label, file_name, data_comment,
data_reference, created_at, updated_at, creator_id, experiment, rating, date_of_announcement,
public, official, date_official, greatest_hit, date_of_run_start, date_of_run_end, `year`
FROM RubyDB.limits;'''

limits_df = pd.read_sql_query(limits_sql, engine)
limits_df['rowid'] = limits_df.index

limits_table_df = limits_df[['rowid','id','spin_dependency',
                             'experiment','official','greatest_hit','data_label',
                             'result_type','data_reference','year']].copy()

limits_table_df['expid'] = limits_table_df['rowid']

limits_metadata_sql = '''SELECT id, spin_dependency, result_type, measurement_type, nomhash, x_units, y_units, x_rescale, y_rescale, default_color, default_style, data_label, file_name, data_comment, data_reference, created_at, updated_at, creator_id, experiment, rating, date_of_announcement, public, official, date_official, greatest_hit, date_of_run_start, date_of_run_end, `year`
FROM `data`.limits_metadata;'''

limits_metadata_df = pd.read_sql_query(limits_metadata_sql, engine)
limits_metadata_df['rowid'] = limits_metadata_df.index

#####

limits_traces_sql = '''SELECT distinct limit_id, trace_id, trace_name FROM `data`.limits_data;;'''
limits_traces_df = pd.read_sql_query(limits_traces_sql, engine)
limits_traces_df['rowid'] = limits_traces_df.index

#####

limits_data_sql = '''SELECT id, limit_id, trace_id, trace_name, x, y FROM `data`.limits_data;;'''

limits_data_df = pd.read_sql_query(limits_data_sql, engine)
limits_data_df['rowid'] = limits_data_df.index

#####

limit_types_list = ['All Limits', 'Official Limits']
limit_types_df = pd.DataFrame(data=limit_types_list,columns=['label'])
#limit_types_df

years = list(range(2001,2023))
#years = map(str, range(2001, 2023))

years_df = pd.DataFrame(data=years,columns=['year'])
#years_df['rowid'] = years_df.index
#years_df
#years_dict = years_df.to_dict('records')
#years_dict

###########################################################################

table_heights = 120

style_header_var={ 'backgroundColor': 'black','color': 'white'}

years_table = dash_table.DataTable(
    id='years_table',
    columns=[
        {'name': 'Year', 'id': 'year', 'type': 'numeric'},
    ],
    data=years_df.to_dict('records'),
    filter_action='none',
    row_selectable='multi',
    fixed_rows={'headers': True},
    #page_size=3,
    style_cell_conditional=[
        {'if': {'column_id': 'year'},
         'width': '90%'},
    ],
    style_cell={'textAlign': 'left','padding': '0px','font_size': '12px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 12px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    selected_rows=[],
    style_table={
        'height': table_heights,
    },
    style_header=style_header_var,
    #style_data={
    #    'width': '25px', 'minWidth': '25px', 'maxWidth': '25px',
    #    ##'overflow': 'hidden',
    #    ##'textOverflow': 'ellipsis',
    #}
)

limit_types_table = dash_table.DataTable(
    id='limit_types_table',
    columns=[
        {'name': 'Limit Type', 'id': 'label', 'type': 'text'},
    ],
    data=limit_types_df.to_dict('records'),
   filter_action='none',
    row_selectable='multi',
    #page_size=5,
    style_cell_conditional=[
        {'if': {'column_id': 'label'},
         'width': '90%'},
    ],
    fixed_rows={'headers': True},
    style_cell={'textAlign': 'left','padding': '0px','font_size': '12px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 12px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    selected_rows=[],
    style_table={
        'height': table_heights,
    },
    style_header=style_header_var,
    #style_data={
     #   'width': '25px', 'minWidth': '25px', 'maxWidth': '25px',
     #   ##'overflow': 'hidden',
    #    ##'textOverflow': 'ellipsis',
    #}
)

experiments_table = dash_table.DataTable(
    id='experiments_table',
    columns=[
        {'name': 'Experiment', 'id': 'label', 'type': 'text'},
    ],
    data=experiments_df.to_dict('records'),
   filter_action='none',
    row_selectable='multi',
    #page_size=5,
    style_cell_conditional=[
        {'if': {'column_id': 'Experiment'},
         'width': '90%'},
    ],
    fixed_rows={'headers': True},
    style_table={'height': table_heights},  # defaults to 500
    style_cell={'textAlign': 'left','padding': '0px','font_size': '12px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 12px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    selected_rows=[],
    style_header=style_header_var,
    #style_data={
    #    'width': '25px', 'minWidth': '25px', 'maxWidth': '25px',
    #    ##'overflow': 'hidden',
    #    ##'textOverflow': 'ellipsis',
    #}
)

result_types_table = dash_table.DataTable(
    id='result_types_table',
    columns=[
        {'name': 'ResultType', 'id': 'label', 'type': 'text'},
    ],
    data=result_types_df.to_dict('records'),
    filter_action='none',
    row_selectable='multi',
    #page_size=5,
    style_cell_conditional=[
        {'if': {'column_id': 'ResultType'},
         'width': '90%'},
    ],
    style_cell={'textAlign': 'left','padding': '0px','font_size': '12px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 12px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    fixed_rows={'headers': True},
    selected_rows=[],
    style_table={
        'height': table_heights,
    },
    style_header=style_header_var,
    #style_data={
    #    'width': '25px', 'minWidth': '25px', 'maxWidth': '25px',
    #    ##'overflow': 'hidden',
    #    ##'textOverflow': 'ellipsis',
    #}
)

spin_dependency_table = dash_table.DataTable(
    id='spin_dependency_table',
    columns=[
        {'name': 'SpinDependency', 'id': 'label', 'type': 'text'},
    ],
    data=spin_dependency_df.to_dict('records'),
    filter_action='none',
    row_selectable='multi',
    #page_size=5,
    style_cell_conditional=[
        {'if': {'column_id': 'SpinDependency'},
         'width': '90%'},
    ],
    style_cell={'textAlign': 'left','padding': '0px','font_size': '12px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 12px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    fixed_rows={'headers': True},
    selected_rows=[],
    style_table={
        'height': table_heights,
    },
    style_header=style_header_var,
    #style_data={
    #    'width': '25px', 'minWidth': '25px', 'maxWidth': '25px',
    #    ##'overflow': 'hidden',
    #    ##'textOverflow': 'ellipsis',
    #}
)

greatest_hit_table = dash_table.DataTable(
    id='greatest_hit_table',
    columns=[
        {'name': 'GreatestHit', 'id': 'label', 'type': 'text'},
    ],
    data=greatest_hit_df.to_dict('records'),
    #page_size=5,
    fixed_rows={'headers': True},
    filter_action='none',
    row_selectable='multi',
    selected_rows=[],
    style_cell_conditional=[
        {'if': {'column_id': 'SpinDependency'},
         'width': '90%'},
    ],
    style_cell={'textAlign': 'left','padding': '0px','font_size': '12px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
                'border': '1px solid black'
        },
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 12px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    style_table={'height': table_heights,},
    style_header=style_header_var,
    #style_data={
    #    'width': '25px', 'minWidth': '25px', 'maxWidth': '25px',
        ##'overflow': 'hidden',
        ##'textOverflow': 'ellipsis',
    #}
)

limits_table = dash_table.DataTable(
    id='limits_table',
    data=limits_table_df.to_dict('records'),
    columns=[{'name': 'expid', 'id': 'expid'},
             {'name': 'data_reference', 'id': 'data_reference'},
             {'name': 'data_label', 'id': 'data_label'},
             #{'name': 'experiment', 'id': 'experiment'},
             #{'name': 'spin_dependency', 'id': 'spin_dependency'},
             #{'name': 'result_type', 'id': 'result_type'},
             #{'name': 'year', 'id': 'year'},
             ],
    #fixed_rows={'headers': True},
    page_size=5,
    filter_action='none',
    #row_selectable='multi',
    #selected_rows=[],
    style_cell={'textAlign': 'left','padding': '0px','font_size': '12px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 15px;
            max-height: 45px; min-height:30px; height: 30px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    style_table={'height': '25vh',},
    style_cell_conditional=[
        {'if': {'column_id': 'expid'},
         'width': '5%'},
        {'if': {'column_id': 'data_reference'},
         'width': '20%'},
        {'if': {'column_id': 'data_label'},
         'width': '35%'},
    ],
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    style_header=style_header_var,
    #tooltip_data=[
    #    {
    #        column: {'value': str(value), 'type': 'markdown'}
    #        for column, value in row.items()
    #    } for row in data
    #],
    tooltip_duration=None,
)

plots_table_df = pd.DataFrame(data=None, columns=['expid','data_reference','data_label'])
plots_table_df.set_index('expid')

plots_table = dash_table.DataTable(
    id='plots_table',
    data=plots_table_df.to_dict('records'),
    columns=[{'name': 'tablerowid', 'id': 'tablerowid'},
             {'name': 'expid', 'id': 'expid'},
             {'name': 'data_reference', 'id': 'data_reference'},
             {'name': 'data_label', 'id': 'data_label'},
             #{'name': 'spin_dependency', 'id': 'spin_dependency'},
             #{'name': 'result_type', 'id': 'result_type'},
             #{'name': 'year', 'id': 'year'},
             ],
    #fixed_rows={'headers': True},
    page_size=4,
    style_cell={'textAlign': 'left','padding': '0px','font_size': '12px',
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
    css=[{
        'selector': '.dash-spreadsheet td div',
        'rule': '''
            line-height: 15px;
            max-height: 45px; min-height:30px; height: 30px;
            display: block;
            overflow-y: hidden;
        '''
    }],
    #sort_action='native',
    #sort_mode='multi',
    #sort_as_null=['', 'No'],
    #sort_by=[{'column_id': 'expid', 'direction': 'desc'}],
    filter_action='none',
    row_deletable=True,
    #row_selectable='multi',
    #selected_rows=[],
    style_table={'height': '25vh',},
    style_cell_conditional=[
        {'if': {'column_id': 'expid'},
         'width': '5%'},
        {'if': {'column_id': 'tablerowid'},
         'width': '5%'},
        {'if': {'column_id': 'data_reference'},
         'width': '20%'},
        {'if': {'column_id': 'data_label'},
         'width': '35%'},
    ],
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
    style_header=style_header_var,
)
