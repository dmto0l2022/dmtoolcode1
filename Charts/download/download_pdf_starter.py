##https://community.plotly.com/t/how-to-download-a-pdf-file-generated-from-a-plot/33432/4

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from plotly.io import write_image
import plotly.graph_objs as go
import flask
import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    dcc.Loading(html.A(
        id="img-download", 
        href="", 
        children=[html.Button("Download Image", id="download-btn")], 
        target="_blank",
        download="my-figure.pdf"
    )),
    dcc.Graph(
        id='graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'scatter'},
            ],
            'layout': {'title': 'So Title'}
        }
    )
])

@app.callback(Output('img-download', 'href'),
              [Input('graph', 'figure')])
def make_image(figure):
    """ Make a picture """

    fmt = "pdf"
    mimetype = "application/pdf"
    filename = "figure.%s" % fmt

    write_image(figure, "assets/plots/" + filename)
    data = base64.b64encode(open("assets/plots/" + filename, "rb").read()).decode("utf-8")
    pdf_string = f"data:{mimetype};base64,{data}"

    return pdf_string

if __name__ == '__main__':
    app.run_server(debug=False)
