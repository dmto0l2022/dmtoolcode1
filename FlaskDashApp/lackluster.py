from flask import Flask
from dash import Dash
from dash import dcc
from dash import html


server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    url_base_pathname='/dash'
)

app.layout = html.Div('Lack Luster Dash App', id='dash-container')


@server.route("/dash")
def my_dash_app():
    return app.index()


if __name__ == '__main__':
    app.run_server(debug=True)
