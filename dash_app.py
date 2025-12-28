import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load your formatted CSV
df = pd.read_csv("formatted_output.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sort by Date
df = df.sort_values('Date')

# Create Dash app
app = Dash(__name__)

# Create line chart
fig = px.line(df, x='Date', y='Sales', title='Pink Morsel Sales Over Time')

fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Sales',
    title_x=0.5
)

# Layout of the app
app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={'textAlign': 'center'}),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)