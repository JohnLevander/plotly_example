from math import pi
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import numpy as np
import plotly.express as px

'''
1. brew install conda
2. cd to your development directory
3. conda create --name any_name_you_want (e.g. smh-python-plots)
4. conda activate any_name_you_want (from above)
4. conda install plotly
5. conda install pandas
6. conda install dash
7. python app.py
8. open http://127.0.0.1:8050/
'''

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Plotly Example for Lucie'),
    html.P("Select line color:"),
    dcc.Dropdown(
        id="color-dropdown",
        options=['blue', 'red'],
        value='blue',
        clearable=False,
    ),
    html.P("Select function:"),
    dcc.Dropdown(
        id="sincos-dropdown",
        options=['sin', 'cos'],
        value='sin',
        clearable=False,
    ),
    dcc.Graph(id="the-graph"),
])


@app.callback(
    Output("the-graph", "figure"),
    Input("color-dropdown", "value"),
    Input("sincos-dropdown", "value"))
def display_color(color, sin_or_cos):
    x = np.linspace(-2 * pi, 2 * pi, 1000)
    df = pd.DataFrame(dict(x=x, sin=np.sin(x), cos=np.cos(x)))
    pd.options.plotting.backend = "plotly"
    fig = px.line(df, x='x', y=df.columns[1:3]).update_traces(visible="legendonly",
                                                              selector=lambda t: not t.name in [sin_or_cos])
    fig.data[0].line.color = color
    fig.data[1].line.color = color
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
