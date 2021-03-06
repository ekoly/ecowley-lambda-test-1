import os

from flask import Flask
import dash
import dash_core_components as dcc
import dash_html_components as html

import numpy as np
from plotly import graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
application = Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=application)


app.layout = html.Div([
    html.H2("Hello World!"),
    html.Div([  
        html.Div([  
            dcc.Dropdown(
                id="dropdown",
                options=[{"label": x, "value": x} for x in ["LA", "NYC", "MTL"]],
                value="LA",
            )
        ], className="container four columns"),
        html.Div([
            dcc.Graph(id="value-graph"),
        ], className="container eight columns"),
    ], className="container")
])



def randInts():
    return np.random.randint(0, 100, 100)


points = {
        "LA": go.Scatter(
            x=randInts(),
            y=randInts(),
            mode="markers",
            marker={"color": "red"},
        ),
        "NYC": go.Scatter(
            x=randInts(),
            y=randInts(),
            mode="markers",
            marker={"color": "blue"},
        ),
        "MTL": go.Scatter(
            x=randInts(),
            y=randInts(),
            mode="markers",
            marker={"color": "green"},
        ),
}



@app.callback(
        dash.dependencies.Output("value-graph", "figure"),
        [dash.dependencies.Input("dropdown", "value")],
)
def displayValue(value):
    return go.Figure(data=points[value])


if __name__ == "__main__":
    application.run()
