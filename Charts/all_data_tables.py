from sqlalchemy import create_engine
import pandas as pd

from dash import dash_table

#import psycopg2
engine = create_engine('mysql://pythonuser:pythonuser@localhost:3306/RubyDB')

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

years_table = dash_table.DataTable(
    id='years_table',
    columns=[
        {'name': 'Year', 'id': 'year', 'type': 'numeric'},
    ],
    data=years_df.to_dict('records'),
    filter_action='native',
    row_selectable='multi',
    fixed_rows={'headers': True},
    #page_size=5,
    style_cell_conditional=[
        {'if': {'column_id': 'year'},
         'width': '90%'},
    ],
    style_cell={'textAlign': 'left'},
    selected_rows=[],
    style_table={
        'height': 250,
    },
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
    filter_action='native',
    row_selectable='multi',
    #page_size=5,
    style_cell_conditional=[
        {'if': {'column_id': 'label'},
         'width': '90%'},
    ],
    fixed_rows={'headers': True},
    style_cell={'textAlign': 'left'},
    selected_rows=[],
    style_table={
        'height': 250,
    }
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
    filter_action='native',
    row_selectable='multi',
    #page_size=5,
    style_cell_conditional=[
        {'if': {'column_id': 'Experiment'},
         'width': '90%'},
    ],
    fixed_rows={'headers': True},
    style_table={'height': 250},  # defaults to 500
    style_cell={'textAlign': 'left'},
    selected_rows=[]
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
    filter_action='native',
    row_selectable='multi',
    #page_size=5,
    style_cell_conditional=[
        {'if': {'column_id': 'ResultType'},
         'width': '90%'},
    ],
    style_cell={'textAlign': 'left'},
    fixed_rows={'headers': True},
    selected_rows=[],
    style_table={
        'height': 250,
    }#,
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
    filter_action='native',
    row_selectable='multi',
    #page_size=5,
    style_cell_conditional=[
        {'if': {'column_id': 'SpinDependency'},
         'width': '90%'},
    ],
    style_cell={'textAlign': 'left'},
    fixed_rows={'headers': True},
    selected_rows=[],
    style_table={
        'height': 250,
    }
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
    filter_action='native',
    row_selectable='multi',
    selected_rows=[],
    style_cell_conditional=[
        {'if': {'column_id': 'SpinDependency'},
         'width': '90%'},
    ],
    style_cell={'textAlign': 'left'},
    style_table={'height': 250,}
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
             #{'name': 'spin_dependency', 'id': 'spin_dependency'},
             #{'name': 'result_type', 'id': 'result_type'},
             #{'name': 'year', 'id': 'year'},
             ],
    #fixed_rows={'headers': True},
    page_size=5,
    filter_action='native',
    #row_selectable='multi',
    #selected_rows=[],
    style_table={'height': 300,},
    style_cell_conditional=[
        {'if': {'column_id': 'expid'},
         'width': '5%'},
        {'if': {'column_id': 'data_reference'},
         'width': '45%'},
        {'if': {'column_id': 'data_label'},
         'width': '45%'},
    ],
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
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
    #sort_action='native',
    #sort_mode='multi',
    #sort_as_null=['', 'No'],
    #sort_by=[{'column_id': 'expid', 'direction': 'desc'}],
    filter_action='native',
    row_deletable=True,
    #row_selectable='multi',
    #selected_rows=[],
    style_table={'height': 300,},
    style_cell_conditional=[
        {'if': {'column_id': 'expid'},
         'width': '5%'},
        {'if': {'column_id': 'tablerowid'},
         'width': '5%'},
        {'if': {'column_id': 'data_reference'},
         'width': '40%'},
        {'if': {'column_id': 'data_label'},
         'width': '45%'},
    ],
    style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
)
