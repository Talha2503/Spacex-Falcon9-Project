"""
Lab 7: Interactive Visual Analytics — Plotly Dash App

Run locally with:  python spacex_dash_app.py
Then open the URL it prints (usually http://127.0.0.1:8050) in your browser.

This does NOT run inside Colab well (Dash needs a persistent local server).
Run this on your own machine, or use Google Colab's ngrok/JupyterDash workaround
if you want it inside a notebook. For the assignment, running it locally and
taking a screenshot (or screen-recording) for your slides is the simplest path.
"""

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import os

# ---- Load data ----
if os.path.exists('dataset_part_2.csv'):
    spacex_df = pd.read_csv('dataset_part_2.csv')
else:
    print('dataset_part_2.csv not found locally, loading from IBM dataset repository...')
    fallback_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv'
    spacex_df = pd.read_csv(fallback_url)

max_payload = spacex_df['PayloadMass'].max()
min_payload = spacex_df['PayloadMass'].min()

launch_sites = spacex_df['LaunchSite'].unique().tolist()
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + \
               [{'label': site, 'value': site} for site in launch_sites]

# ---- Build app ----
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 32}),

    dcc.Dropdown(
        id='site-dropdown',
        options=site_options,
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True
    ),
    html.Br(),

    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
        value=[min_payload, max_payload]
    ),

    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        fig = px.pie(
            spacex_df, values='Class', names='LaunchSite',
            title='Total Successful Launches by Site'
        )
    else:
        filtered_df = spacex_df[spacex_df['LaunchSite'] == selected_site]
        outcome_counts = filtered_df['Class'].value_counts().reset_index()
        outcome_counts.columns = ['Class', 'count']
        outcome_counts['Class'] = outcome_counts['Class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(
            outcome_counts, values='count', names='Class',
            title=f'Success vs. Failure for site {selected_site}'
        )
    return fig


@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_chart(selected_site, payload_range):
    low, high = payload_range
    mask = (spacex_df['PayloadMass'] >= low) & (spacex_df['PayloadMass'] <= high)
    filtered_df = spacex_df[mask]

    if selected_site != 'ALL':
        filtered_df = filtered_df[filtered_df['LaunchSite'] == selected_site]

    fig = px.scatter(
        filtered_df, x='PayloadMass', y='Class',
        color='BoosterVersion',
        title='Payload Mass vs. Launch Outcome',
        labels={'Class': 'Landing Outcome (1=Success, 0=Failure)'}
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True)
