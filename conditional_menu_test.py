import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

eng_esp_options:{'age':{
    'Menor de 18 años':'age_less_than_18',
    'Mayor de 18 años':'age_more_than_18',
    '18 - 59 años':'age_18_to_59',
    'Mayor de 60 años':'age_more_than_60',
    '18 - 24 años':'age_18_to_24',
    '25 - 34 años':'age_25_to_34',
    '35 – 44 años':'age_35_to_44',  '45 –55 años':'age_45_to_55',  
    'Mayor de 55 años':'age_more_than_55'
    }, 
    'travel':{
    'Solo/a': 'travel_alone',
    'Acompañado/a' : 'travel_accompanied'
    }, 
    'gender':{
    'Femenino': 'gender_female',
    'Masculino': 'gender_male',
    'Otro': 'gender_other',
    'Intersexual': 'gender_intersex'    
}
}

age_options = {'Perú': [('Menor de 18 años'), 
('18 - 59 años'),
('Mayor de 60 años')],
'México':[('18 - 24 años'),
('25 - 34 años'),
('35 – 44 años'),
('45 –55 años')],
'Ecuador':[
('Menor de 18 años'),
('Mayor de 18 años')]}


country_list = ['Perú', 'México', 'Ecuador']

gender_options = {'Perú':['Femenino', 'Masculino','Otro'], 
'México':['Femenino', 'Masculino','Otro'], 
'Ecuador':['Femenino', 'Masculino','Intersexual']}


travel_options = ['travel_alone', 'travel_accompanied']


### App Interface Layout

app.layout = html.Div([
    dcc.Tabs(id='tabs-example', value='Perú', children=[
        dcc.Tab(label='Perú', value='Perú'),
        dcc.Tab(label='México', value='México'),
        dcc.Tab(label='Ecuador', value='Ecuador'),
    ]),
    html.Div(id='all_dropdowns', children=[
        html.Div(className='user_dropdowns', 
            children=[
            html.H3('Filtros de Usuarios'),
            html.P('Edad', className="lead"),
            dcc.Dropdown(id='age-dropdown', value='All'),
            html.P('Genero', className="lead"),
            dcc.Dropdown(id='gender-dropdown',
                value='All'),
            html.P('Travel Status', className="lead"),
            dcc.Dropdown(id='travel-dropdown', 
                options=[{'label': 'Acompañado/a', 'value':'travel_accompanied'},
                         {'label': 'Solo/a', 'value': 'travel_alone'}],
                                value='All')
            ],
            style={'width': '40%'}),
            html.Div(id='display-selected-values'),
        html.Div(className='other_dropdowns', 
            children=[
                html.H3('Otros Filtros'),
                html.P('Edad2', className="lead"),
                dcc.Dropdown(id='age-dropdown2', value='All'),
                html.P('Genero2', className="lead"),
                dcc.Dropdown(id='gender-dropdown2',
                    value='All'),
                html.P('Travel Status2', className="lead"),
                dcc.Dropdown(id='travel-dropdown2', 
                    options=[{'label': 'Acompañado/a', 'value':'travel_accompanied'},
                             {'label': 'Solo/a', 'value': 'travel_alone'}],
                                    value='All')
                ],
            style={'width': '40%', 'display': 'inline-block'}),
    ], style={'display': 'flex',
    'justify-content': 'space-evenly'})
])

### Three Dropdowns Setup with link to Country

@app.callback(
    Output('age-dropdown', 'options'),
    [Input('tabs-example', 'value')])
def set_age_options(selected_country):
    return [{'label': i, 'value': i} for i in age_options[selected_country]]


@app.callback(
    Output('gender-dropdown', 'options'),
    [Input('tabs-example', 'value')])
def set_gender_options(selected_country):
    return [{'label': i, 'value': i} for i in gender_options[selected_country]]

### Final Message


if __name__ == '__main__':
    app.run_server(debug=True)