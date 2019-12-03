import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pickle_file.classific import Classific

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Prudential Insurance Assessment'),
        html.P('This application used to determine whether the user could apply for a insurance or not.'),
    

    html.Label('Gender'),
    dcc.RadioItems(
        id='input-gender',
        options=[
            {'label': 'Male', 'value': 1},
            {'label': 'Female', 'value': 2},
        ],
        value=0,labelStyle={'margin-right': 30}),
    html.Br(),
    
    html.Label('Age'),
    dcc.RadioItems(
        value=2,id='input-age',
        options=[
            {'label': '< 28 years old', 'value': -1},
            {'label': '28 - 56 years old', 'value': 0},
            {'label': '> 56 years old', 'value': 1}
        ],
        labelStyle={'margin-right': 30}),
    html.Br(),
    
    html.Label('Height'),
    dcc.RadioItems(
        value=2,id='input-height',
        options=[
            {'label': '< 160 cm (men) or < 155 cm (women)', 'value': -1},
            {'label': '160 cm - 180 cm (men) or 155 cm - 175 cm (women)', 'value': 0},
            {'label': '> 180 cm (men) or > 175 cm (women)', 'value': 1}
        ],
        labelStyle={'margin-right': 30}),
    html.Br(),
    
    html.Label('Weight'),
    dcc.RadioItems(
        value=2,id='input-weight',
        options=[
            {'label': '< 60 kg (men) or < 55 kg (women)', 'value': -1},
            {'label': '60 - 85 kg (men) or 55 - 70 kg (women)', 'value': 0},
            {'label': '> 85 kg (men) or > 70 kg (women)', 'value': 1}
        ],
        labelStyle={'margin-right': 30}),
    html.Br(),
    
    html.Label('BMI'),
    dcc.RadioItems(
        value=2,id='input-bmi',
        options=[
            {'label': 'Underweight (< 18.5)', 'value': -1},
            {'label': 'Normal (18.5 - 25)', 'value': 0},
            {'label': 'Overweight (> 25)', 'value': 1}
        ],
        labelStyle={'margin-right': 30}),
    html.Br(),
    
    html.Label('Current Work Duration (years) '),
    dcc.Input(id='input-employ-info',value=0, type='number'),
    html.Br(),html.Br(),
        
    html.Label('Marital Status'),
    dcc.RadioItems(
        value=0,id='input-insur-info',
        options=[
            {'label': 'Unmarried', 'value': 1},
            {'label': 'Married (without children)', 'value': 2},
            {'label': 'Married (with children)', 'value': 3}
        ],
        labelStyle={'margin-right': 30}),
    html.Br(),
    
    html.Label('Number of Children'),
    dcc.RadioItems(
        value=0,id='input-fam-hist',
        options=[
            {'label': '0', 'value': 1},
            {'label': '1-2', 'value': 2},
            {'label': '>2', 'value': 3}
        ],
        labelStyle={'margin-right': 110}),
    html.Br(),
    
    html.Label('Medical History'),
    dcc.RadioItems(
        value=0,id='input-med-hist',
        options=[
            {'label': 'Does not carry hereditary disease(s)', 'value': 1},
            {'label': 'Has hereditary disease(s)', 'value': 2},
            {'label': 'Dont know', 'value': 3}
        ],
        labelStyle={'margin-right': 10}),
    html.Br(),
        
    html.Label('Number of Hospitalization in 4 months '),
    dcc.Input(id='input-med-key',value=0, type='number'),
    html.Br(),html.Br(),
    
    html.Button('See The Result', id='show-secret'),
    html.Div(id='body-div'),
    html.Br(),html.Br(),
])

classific = Classific()
    
@app.callback(
    Output("body-div", "children"),
    [Input("show-secret", "n_clicks")],
    [State("input-gender", "value"),
    State("input-age", "value"),
    State("input-height", "value"),
    State("input-weight", "value"),
    State("input-bmi", "value"),
    State("input-employ-info", "value"),
    State("input-insur-info", "value"),
    State("input-fam-hist", "value"),
    State("input-med-hist", "value"),
    State("input-med-key", "value")]
    )
    
def process_data(n_clicks: int, 
                 gender: int, age: int, weight: int, height: int, bmi: int,
                 employ_info: int, insur_info: int, fam_hist: int,
                 med_hist: int, med_key: int):
                     
        
    data = classific.classify(
            gender=gender,
            age=age,
            height=height,
            weight=weight,
            bmi=bmi,
            employ_info=employ_info,
            insur_info=insur_info,
            fam_hist=fam_hist,
            med_hist=med_hist,
            med_key=med_key
        )
    #return data
    
    if n_clicks is None:
        raise PreventUpdate
    elif data==0:
        return "You\'re Not Qualified for Receiving the Standard Insurance Policy"
    elif data==1:
        return "You\'re Qualified for Receiving the Standard Insurance Policy"
    else:
        return "Error 404 Not Found"
        
if __name__ == '__main__':
    app.run_server(debug=True)