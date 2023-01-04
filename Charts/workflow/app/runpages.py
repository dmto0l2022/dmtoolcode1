from dash import Dash, html, dcc
import dash
import dash_bootstrap_components as dbc

#app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

app = Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP])

##print(dash.page_container)
'''
page_container = html.Div([dcc.Location(id='_pages_location'),
                           html.Div(id='_pages_content',
                           style={"height": "50%", "width": "100%","border": "4px solid black" , "text-align": "center",
                           "background-color": "red",
                           ##"display": "inline-block", "vertical-align": "middle"
                           ##"display" : "flex", "align-items" : "center"
                           "display" : "table"
                           }),
                           dcc.Store(id='_pages_store'),
                           html.Div(id='_pages_dummy', style={"height": "10%", "width": "100%","border": "1px solid black" , "background-color": "orange"})],
                           style={"height": "60%", "width": "100%","border": "1px solid black" , "background-color": "yellow"}
                           )
'''

row = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div("Left"),style={"border":"2px black solid", "text-align": "left"}),
                dbc.Col(html.Div("Middle"),style={"border":"2px black solid", "text-align": "center"}),
                dbc.Col(html.Div("Right"),style={"border":"2px black solid", "text-align": "right"}),
            ],
            style={"height": "50%", "width": "100%","border": "1px solid black" , "background-color": "red"}),
        dbc.Row(
            [
                dbc.Col(html.Div("Middle"),style={"border":"2px black solid", "text-align": "center 2", "height": "50%"}, width=6, align="center"),
            ],
            style={"height": "50%", "width": "100%","border": "1px solid black" , "background-color": "cyan"},  justify="center"),
       ],
 style={"height": "100vh", "width": "100vw","border": "1px solid black" , "background-color": "yellow"},
 className = "container-fluid")


'''
layout_1 = html.Div([
    html.Div('Multi-page app with Dash Pages', style={"height": "5%", "width": "100%"} ),
    html.Div(
        [
            html.Div(
                dcc.Link(
                    f"{page['name']} - {page['path']}", href=page["relative_path"]
                )
            )
            for page in dash.page_registry.values()
        ], style={"height": "30%", "width": "100%", "background-color": "grey",  "border": "1px solid red"}
    ),
	#html.Div(dash.page_container, style={"height": "50%", "width": "100%","border": "5px solid black" , "background-color": "purple"})
	##page_container,
	row,
	html.Div('footer', style={"height": "5%", "width": "100%"} ),
], style={"height": "90vh", "width": "90vw", "background-color": "green", "border": "1px solid black"})
'''

app.layout = row

layout_bs = layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)



if __name__ == '__main__':
	app.run_server(debug=True)
