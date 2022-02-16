import altair as alt
from dash import Dash, dcc, html, Input, Output

from vega_datasets import data

iris = data.iris()

app = Dash(__name__)
app.layout = html.Div([
        html.Div([
            html.P("X:", style={"float":"left"}),
            html.Div(
                dcc.Dropdown(
                    id='xcol', value=iris.columns[0],
                    options=[{'label': i, 'value': i} for i in iris.columns[:-1]],
                    style={"width": "100%"},
                    clearable = False),
                style={"float":"left", "width": "40%"}
            ),
            html.P("Y:", style={"float":"left", "margin-left":"10px"}),
            html.Div(
                dcc.Dropdown(
                    id='ycol', value=iris.columns[1],
                    options=[{'label': i, 'value': i} for i in iris.columns[:-1]],
                    style={"float":"left", "width": "100%"},
                    clearable = False),
                style={"float":"left", "width": "40%"}
            )
            ],
            style={"width": "35%", "float":"left"} 
        ),

        html.Iframe(
            id="scatter",
            style={"border-width": '0', 'width':"100%", "height":"400px"}
        )])

@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol', 'value'),
    Input('ycol', 'value'),
    )
def plot_iris(xcol, ycol):
    assert xcol in iris.columns, f"{xcol} not found in iris dataset"
    assert ycol in iris.columns, f"{ycol} not found in iris dataset"
    chart = alt.Chart(iris, title=f"{ycol} vs {xcol}").mark_point().encode(
        x=xcol,
        y=ycol,
        color="species"
    )
    return chart.to_html()


if __name__ == '__main__':
    app.run_server(debug=True)