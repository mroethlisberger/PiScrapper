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

    # create graph for every df
    graphs.append(
    dcc.Graph(id=f"timeseries-{product}",
            config={'displayModeBar': False},
            animate=True,
            figure=px.line(df,
                x='Time',
                y='Price',
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
        html.P('''ToDo: Yes''')
    ]),

    html.Div(className='eight columns div-for-charts bg-grey',  # Define the right element
    children=graphs
    )
])



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
