import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import os


"""
ToDO:
    - callculate average Price over one day
    - beatuify the x-axis
    - add menubar on the left:
        - sort by category
        - add url + category to wishlist
    - setup a clean "productive" environment
    - add git.ignore
"""

# df = pd.read_csv('./digitec/Ryzen 7 5800X (AM4, 3.80GHz, 8-Core).csv',  sep=",")

path = './data/'
df = pd.DataFrame()
data = pd.DataFrame()
files = []

# r=root, d=directories, f=files
for r, d, f in os.walk(path):
    for file in f:
        if ".DS_Store" and "wishlist" not in file:
            files.append(os.path.join(r, file))


# dynamic list of graphs for every product in data folder
graphs = []
for product in files:
    # read every csv based on files-list
    df = pd.read_csv(product, sep=",")
    
    # for debugging
    # print(df)

    position_slash = product.find('\\')
    product_name = product[position_slash+1:-4]

    # create graph for every df
    graphs.append(
    dcc.Graph(id=f"timeseries-{product}",
            config={'displayModeBar': False},
            animate=True,
            figure=px.line(df,
                x='Time',
                y='Price',
                title=product_name,
                template='plotly_dark').update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                        'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
        )
    )



# Initialise the app
app = dash.Dash(__name__)

# Define the app
app.layout = html.Div(children=[
    html.Div(className='four columns div-user-controls',  # Define the left element
    children = [
        html.H2('Dash - HUGE PP POWER'),
        html.P('''Visualising digitec prices with Plotly - Dash'''),
        html.P('''ToDo: Yes'''),
        # dcc.Input(id="input", type="text", placeholder="", debounce=True),
        # html.Div(id="output"),

        html.Div(dcc.Input(id='input-on-submit', type='text')),
        html.Button('Submit', id='submit-val', n_clicks=0),
        html.Div(id='container-button-basic',
            children='Enter a value and press submit'),
    ]),

    html.Div(className='eight columns div-for-charts bg-grey',  # Define the right element
    children=graphs
    )
])

@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-on-submit', 'value')])
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )

# @app.callback(
#     Output("output", "children"),
#     Input("input", "value"),
# )
# def update_output(input1):
#     return u'Input {}'.format(input1)


# Run the app
if __name__ == '__main__':
    app.run_server(host= '127.0.0.5', port=8051, debug=True)
