import dash #creating a webpage
import dash_core_components as dcc #visual component
import dash_html_components as html
import plotly.graph_objs as go #employ graphics
from dash.dependencies import Input, Output, State #calling the library


list_of_types=['Brick', 'Plate', 'Tile']
list_of_sizes=['1X2', '2X2', '2X4']


########### Initiate the app (setting up html and css)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets) #for dash to get the url to display the css style sheet
server = app.server
app.title='LEGO Pieces'

########### Set up the layout

app.layout = html.Div(children=[
    html.Br(),
    html.H3('Which LEGO piece you will choose?'),
    html.Div([
        html.Div([
            dcc.RadioItems(
                id='pick-a-type',
                options=[
                        {'label':list_of_types[0], 'value':list_of_types[0]},
                        {'label':list_of_types[1], 'value':list_of_types[1]},
                        {'label':list_of_types[2], 'value':list_of_types[2]},
                        ],
                value='choose',
                ),
        ],className='two columns'),
        html.Div([
            dcc.RadioItems(
                id='pick-a-size',
                options=[
                        {'label':list_of_sizes[0], 'value':list_of_sizes[0]},
                        {'label':list_of_sizes[1], 'value':list_of_sizes[1]},
                        {'label':list_of_sizes[2], 'value':list_of_sizes[2]},
                        ],
                value='lego',
                ),
        ],className='two columns'),
        html.Div([
            html.Div(id='your_output_here', children=''),
        ],className='eight columns'),
    ],className='twelve columns'),
    html.Br(),
    html.A('Code on Github', href='https://github.com/caroleonor/dash-callbacks-multi-input/edit/master/app.py'),
    html.Br(),
    html.A("Data Source", href='https://brickarchitect.com/book/bricks'),
    ]
)

########## Callback

@app.callback(Output('your_output_here', 'children'),
              [Input('pick-a-type', 'value'),
               Input('pick-a-size', 'value')])
def radio_results(type_you_picked, size_you_picked):
    image_you_chose=f'{type_you_picked}-{size_you_picked}.jpg'
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': 'auto'}),

############ Deploy
if __name__ == '__main__':
    app.run_server()
