# dash_app.py
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# Load formatted CSV
df = pd.read_csv("formatted_output.csv")
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')

app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={
        'textAlign': 'center',
        'color': '#4B0082',
        'font-family': 'Arial',
        'margin-bottom': '30px'
    }),

    html.Div([
        html.Label("Select Region:", style={'margin-right': '10px', 'font-weight': 'bold'}),
        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'margin-right': '15px'}
        )
    ], style={'textAlign': 'center', 'margin-bottom': '20px'}),

    dcc.Graph(id='sales-graph')
], style={'max-width': '900px', 'margin': '0 auto', 'padding': '20px', 'background-color': '#F0F8FF'})

# Callback to update figure
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    # Filter region
    if selected_region == 'all':
        filtered_df = df.copy()
    else:
        filtered_df = df[df['Region'].str.lower() == selected_region.lower()]

    filtered_df = filtered_df.sort_values('Date')

    # Create line chart
    fig2 = px.line(filtered_df, x='Date', y='Sales', title='Pink Morsel Sales Over Time')

    # Add vertical line for price increase (always visible)
    max_y = filtered_df['Sales'].max() if not filtered_df.empty else df['Sales'].max()
    fig2.add_trace(
        go.Scatter(
            x=[pd.to_datetime("2021-01-15"), pd.to_datetime("2021-01-15")],
            y=[0, max_y*1.05],
            mode="lines",
            line=dict(color="red", dash="dash", width=2),
            name="Price Increase"
        )
    )

    fig2.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales',
        title_x=0.5
    )

    return fig2

if __name__ == "__main__":
    app.run()