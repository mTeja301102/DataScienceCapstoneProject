# Import required libraries
import pandas as pd
import dash
#import dash_html_components as html
#import dash_core_components as dcc
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    #TASK 2.1 Add title to the dashboard
    html.H1('SpaceX Launch Records Dashboard',style={'textAlign': 'center', 'color': '#503D36', 'font-size': 24}),
    html.Div([dcc.Dropdown(id="dropdown",
                           options=[{"label" : "All Sites" , "value" : "All Sites"},
                                    {"label" : "CCAFS LC-40" , "value" : "CCAFS LC-40"},
                                    {"label" : "CCAFS SLC-40" , "value" : "CCAFS SLC-40"},
                                    {"label" : "KSC LC-39A" , "value" : "KSC LC-39A"},
                                    {"label" : "VAFB SLC-4E" , "value" : "VAFB SLC-4E"}],
                            placeholder = "Select a Launch Site",
                            value = "All Sites",
                            searchable = True,
                            style = {"width" : "80%" , "padding" : "3px" , "font-size" : "20px" , "textAlign" : "center" },
                            ) 
                ]),
    html.H1('Total successful launches by site',style={'textAlign': 'left', 'color': '#503D36', 'font-size': 18}),
    html.Div([
              html.Div(dcc.Graph(id="plot1"))
             ],
              style = {"display":"flex"}
    ),
    html.H1('Payload Range(kg):',style={'textAlign': 'left', 'color': '#503D36', 'font-size': 18}),
    html.Div([dcc.RangeSlider(id='payload-slider',
                min=0, max=10000, step=1000,
                marks={0: '0',
                       2500: '2500',
                       5000: '5000',
                       7500: '7500',
                       10000: '10000'},
                value=[min_payload, min_payload])
              ],),
    html.Div([
              html.Div(dcc.Graph(id="plot2"),style={"width":"100%"})
             ],
              style = {"display":"flex"}
    ),
])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output(component_id='plot1', component_property='figure'),
    Input(component_id='dropdown',component_property='value')
    )
def update_output_container(launch_site):
    #print(launch_site)
    if(launch_site == "All Sites"):
       g = spacex_df[spacex_df["class"]==1]
       j = g.groupby("Launch Site")["class"].count().reset_index()
       fig = px.pie(j , values="class" , names="Launch Site")
       #return fig
    elif(launch_site == "CCAFS LC-40"):
        h = spacex_df[spacex_df["Launch Site"] == "CCAFS LC-40"]
        k = h["class"].value_counts().reset_index()
        #print(k)
        fig = px.pie(k , values="count" , names="class")
    elif(launch_site == "CCAFS SLC-40"):
        h = spacex_df[spacex_df["Launch Site"] == "CCAFS SLC-40"]
        k = h["class"].value_counts().reset_index()
        #print(k)
        fig = px.pie(k , values="count" , names="class")
    elif(launch_site == "KSC LC-39A"):
        h = spacex_df[spacex_df["Launch Site"] == "KSC LC-39A"]
        k = h["class"].value_counts().reset_index()
        #print(k)
        fig = px.pie(k , values="count" , names="class")
    elif(launch_site == "VAFB SLC-4E"):
        h = spacex_df[spacex_df["Launch Site"] == "VAFB SLC-4E"]
        k = h["class"].value_counts().reset_index()
        #print(k)
        fig = px.pie(k , values="count" , names="class")
    return fig
# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output(component_id='plot2', component_property='figure'),
    [Input(component_id='dropdown', component_property='value'), Input(component_id="payload-slider", component_property="value")]
            )
def scatterplot(launch_site,payload_range):
    if(launch_site == "All Sites"):
        df = spacex_df[(spacex_df["Payload Mass (kg)"]>=payload_range[0]) & (spacex_df["Payload Mass (kg)"]<=payload_range[1])]
        fig = px.scatter(df,x="Payload Mass (kg)",y="class",color="Booster Version")
        #return fig
    elif(launch_site == "CCAFS LC-40"):
        h = spacex_df[spacex_df["Launch Site"] == "CCAFS LC-40"]
        df = h[(h["Payload Mass (kg)"]>=payload_range[0]) & (h["Payload Mass (kg)"]<=payload_range[1])]
        fig = px.scatter(df,x="Payload Mass (kg)",y="class",color="Booster Version")
        #return None
    elif(launch_site == "CCAFS SLC-40"):
        h = spacex_df[spacex_df["Launch Site"] == "CCAFS SLC-40"]
        df = h[(h["Payload Mass (kg)"]>=payload_range[0]) & (h["Payload Mass (kg)"]<=payload_range[1])]
        fig = px.scatter(df,x="Payload Mass (kg)",y="class",color="Booster Version")
    elif(launch_site == "KSC LC-39A"):
        h = spacex_df[spacex_df["Launch Site"] == "KSC LC-39A"]
        df = h[(h["Payload Mass (kg)"]>=payload_range[0]) & (h["Payload Mass (kg)"]<=payload_range[1])]
        fig = px.scatter(df,x="Payload Mass (kg)",y="class",color="Booster Version")
    elif(launch_site == "VAFB SLC-4E"):
        h = spacex_df[spacex_df["Launch Site"] == "VAFB SLC-4E"]
        df = h[(h["Payload Mass (kg)"]>=payload_range[0]) & (h["Payload Mass (kg)"]<=payload_range[1])]
        fig = px.scatter(df,x="Payload Mass (kg)",y="class",color="Booster Version")

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
