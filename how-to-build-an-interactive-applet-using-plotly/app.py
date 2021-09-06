import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv('MTS_RcptSrcOutlyAgcy_20150331_20210731.csv')

df1 = df.loc[df.loc[:,'Data Type Code'] == 'D',['Current Month Receipt or Outlay Amount','Calendar Year','Calendar Month Number','Classification Description','Record Type Code']]

df1 = df1.rename(columns={'Current Month Receipt or Outlay Amount':'Amount','Calendar Year':'Year', 'Calendar Month Number':'Month Num', 'Classification Description':'Description','Record Type Code':'Type'})

df1.loc[df1.loc[:,'Type'].isin(['RSG','SL']),'Type'] = 'Receipt'
df1.loc[df1.loc[:,'Type'].isin(['A','C','P','UORG']),'Type'] = 'Outlay'

df1['Month'] = df1['Year'].astype(str) + '-' + df1['Month Num'].astype(str)

# Here we create the app
# You can specify stylesheets with dash.Dash(__name__, external_stylesheets = [<url>,<url>,...])
app = dash.Dash(__name__)

# Now we create the layout
app.layout = html.Div(children=[
    html.H1('Receipts and Outlays of the U.S. Government'),
    html.Div([
      'Data From ', 
      html.A('U.S. Treasury', href='https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/summary-of-receipts-and-outlays-of-the-u-s-government', target='_blank')
    ]),
    html.Br(),
    html.Hr(),
    html.Div([
      # This dropdown will display 'Receipt' and 'Outlay'
      dcc.Dropdown(
        id='graph-type',
        # options are set with a list of dictionaries with 'label' and 'value' keys
        options=[{'label': i, 'value': i} for i in ['Receipt', 'Outlay']],
        value='Outlay'),
      html.Br(),
      # This RadioItems will display 'Single' and 'Multiple'
      dcc.RadioItems(
        id='series-type',
        # options here are set just like the Dropdown options
        options=[{'label': i, 'value': i} for i in ['Single', 'Multiple']],
        value='Multiple'),
      html.Br(),
      # This Dropdown will be set up with our callbacks
      dcc.Dropdown(id='show-value')
      ],
      # Inline style for an HTML element is passed with a dictionary
      style={'width': '300px', 'display': 'inline-block'}
    ),
    html.Hr(),
    # This Graph will be set up with our callbacks
    dcc.Graph(id='example-graph')
])

@app.callback(
    Output('show-value','style'),
    Input('series-type','value'))
def update_show_value_visibility(series_type):
    if series_type == 'Multiple':
        style = {'visibility':'hidden'}
    else:
        style = {'visibility':'visible'}
    return style

@app.callback(
    Output('show-value','options'),
    Output('show-value','value'),
    Input('graph-type','value'))
def update_show_value_options(graph_type):
    df0 = df1[df1.loc[:,'Type']==graph_type]
    option_types = df0['Description'].unique()
    options = [{'label': i, 'value': i} for i in option_types]
    return options, option_types[0]

@app.callback(
    Output('example-graph', 'figure'),
    Input('series-type','value'),
    Input('graph-type','value'),
    Input('show-value','value'))
def update_example_graph(series_type, graph_type, show_value):
    df0 = df1[df1.loc[:,'Type']==graph_type]
    if series_type == 'Single':
        df0 = df0[df0.loc[:,'Description'] == show_value]
    fig = px.line(df0, x='Month', y='Amount', color='Description', markers=True)
    return fig

if __name__ == '__main__':
    app.run_server()
