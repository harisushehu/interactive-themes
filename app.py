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

# Ensure columns are correctly referenced; adjust names if needed
expected_columns = ['Themes', 'Sector_voice', 'Aka_korero']
missing_columns = [col for col in expected_columns if col not in data.columns]

if missing_columns:
    print(f"Missing columns in the data: {missing_columns}")
else:
    # If columns are present, proceed with processing
    # Melt the data to long format
    data_long = pd.melt(
        data, 
        id_vars=['Themes'], 
        value_vars=['Sector_voice', 'Aka_korero'], 
        var_name='Source', 
        value_name='Text'
    )

    # Create a breakdown of Themes by source
    themes_count = pd.DataFrame({
        'Themes': data['Themes'],
        'Sector_voice_Count': data['Sector_voice'].apply(lambda x: len(str(x).split(','))),
        'Aka_korero_Count': data['Aka_korero'].apply(lambda x: len(str(x).split(',')))
    })


     # Create the second bar chart showing the count of themes from each source
    fig = px.bar(
        themes_count.melt(id_vars='Themes', value_vars=['Sector_voice_Count', 'Aka_korero_Count']),
        x='Themes', 
        y='value', 
        color='variable', 
        title="Themes Count by Sources (Sector Voice vs Aka Korero)",
        labels={'value': 'Count', 'variable': 'Source'}
    )
    
    # Create the first interactive scatter plot
    fig1 = px.scatter(
        data_long, 
        x='Source', 
        y='Themes', 
        color='Source', 
        hover_data=['Text'],
        title='Interactive Clustering of Themes by Source'
    )

   

    # Initialize the Dash app
    app = Dash(__name__)

    # App layout
    app.layout = html.Div([
        html.H1("Interactive Themes Clustering"), 
        dcc.Graph(figure=fig),   # First graph
        dcc.Graph(figure=fig1),   # Second graph
    ])

    # Run the app
    if __name__ == '__main__':
        # Specify host and port
        app.run_server(debug=True, host='0.0.0.0', port=8080)
