from dash.dependencies import Output, Input

def register_callbacks(app):

    @app.callback(Output('output', 'children'), [Input('btn', 'n_clicks')])
    def on_click(n_clicks):
        return 'Clicked {} times'.format(n_clicks)
        
        