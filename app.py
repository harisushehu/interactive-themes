# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:23:40 2024

@author: HarisuShehu
"""

# app.py
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load data
data = pd.read_csv("./Preprocessed_result.csv")
data = pd.melt(data, id_vars=['Themes'], 
               value_vars=['Sector_voice', 'Aka_korero'], 
               var_name='Source', value_name='Text')

# Initialize the Dash app
app = Dash(__name__)

# Create the interactive plot
fig = px.scatter(data, x='Source', y='Themes', 
                 color='Source', hover_data=['Text'],
                 title='Interactive Clustering of Themes by Source')

# App layout
app.layout = html.Div([
    html.H1("Interactive Themes Clustering"),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
