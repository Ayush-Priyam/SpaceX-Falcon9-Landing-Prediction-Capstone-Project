import pandas as pd
import dash
from dash.dependencies import Input, Output
import plotly.express as px
from dash import html
from dash import dcc
import matplotlib.pyplot as plt

# Reading the airline data into dataframes
spacex_df = pd.read_csv("datasets/spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

#Dash application
app = dash.Dash(__name__)

#Creating the layout
app.layout =html.Div(children=[html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center', 'color': 'black', 'font-size': 40, 'font-family': 'Arial'}),
                               html.H2('by Ayush Priyam', style={
                                       'textAlign': 'center', 'color': 'black', 'font-size': 15, 'font-family': 'Arial'}),
                               html.Br(),
                               dcc.Dropdown(id='site-dropdown', options=[
                                    {'label': 'All Sites', 'value': 'ALL'},
                                    {'label': 'CCAFS LC-40',
                                                'value': 'site1'},
                                    {'label': 'CCAFS SLC-40',
                                     'value': 'site2'},
                                    {'label': 'KSC LC-39A',
                                     'value': 'site3'},
                                    {'label': 'VAFB SLC-4E',
                                     'value': 'site4'},
                                ],  value='ALL', placeholder="Select Launch Site", searchable=True,
                                            style={'width': '100%', 'font-size': '20px', 'text-align': 'center'}),
                                html.Br(),

                                # TASK 2: Adding a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart'),
                                         style={"border": "1px black solid", "border-radius": "5px"}),
                                html.Br(),

                                html.P("Payload range (Kg):", style={'font-size': 25, 'font-family': 'Arial'}),
                                # TASK 3: Adding a slider to select payload range
                                html.Div(dcc.RangeSlider(id='payload-slider', min=0, max= 10000, step=1000, value=[min_payload, max_payload]),
                                         style={"border-style": "groove", "border-radius": "5px", "padding-top": "10px"}),
                                html.Br(),
                                # TASK 4: Adding a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart'),
                                         style={"border": "1px black solid", "border-radius": "5px"}, ),
                                ]
                    )

# TASK 2:
# Adding a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
              Input(component_id='site-dropdown', component_property='value'))
#defining the function for the piechart for callback 1
def piechart(entered_site):
    if entered_site == 'ALL':
        #filtering the dataframe by class for all sites.
        aa = spacex_df[spacex_df['class'] == 1].groupby('Launch Site')[['class']].count()
        fig = px.pie(aa, values='class', names=aa.index,
                    title='Total Success Launches by Site')
    else:
        sites = ['CCAFS LC-40', 'CCAFS SLC-40', 'KSC LC-39A', 'VAFB SLC-4E'] #storing the site names in a list
        index = int(entered_site[-1])-1 #accessing the index with the site 
                                    #name as here the last character of the input string is the index. 
                                    # eg 'site1' has last character 1, 'site2' has 2 and so on.
        aa = spacex_df[spacex_df['Launch Site'] == sites[index]]
        bb = aa.groupby('class')[['Launch Site']].count()
        #plotting the pie chart
        fig = px.pie(bb, values='Launch Site', names=bb.index,
                    title=f'Total Success Launches by Site {sites[index]}')
    return fig # return the piechart output for a selected site
        
# TASK 4:
# Adding a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'),
               Input(component_id="payload-slider", component_property="value")])
#defining the function for the scatterplot for callback 2
def scatchart(entered_site, payload):

    df= spacex_df[spacex_df['Payload Mass (kg)'].between(payload[0], payload[1])]
    #if the site is ALL, then plotting the scatterplot for all sites
    if entered_site=='ALL':
        fig = px.scatter(df, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title=f'Payload vs Class for All Sites in range {payload[0]} to {payload[1]}')
    else: 
        #if the site is selected from the dropdown menu
        # then plotting the scatterplot for the selected site.
        sites = ['CCAFS LC-40', 'CCAFS SLC-40', 'KSC LC-39A', 'VAFB SLC-4E']
        index = int(entered_site[-1])-1 #accessing the index with the site name
        df2 = df[df['Launch Site'] == sites[index]] ##filtering the selecetd site
        #plotting the scatterplot
        fig = px.scatter(df2, x='Payload Mass (kg)', y='class', color='Booster Version Category',
                         title=f'Payload vs Class for {sites[index]} in range {payload[0]} to {payload[1]}')
        
    return fig #returning the scatterplot output for the selected site/all sites, range.

# Runing the app
if __name__ == '__main__':
    app.run_server()
