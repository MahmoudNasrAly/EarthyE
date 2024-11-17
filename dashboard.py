import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import numpy as np


class StoreDashboard:
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        self.app = Dash(__name__)

    def load_data(self):
        """Load and preprocess the data"""
        self.df = pd.read_excel(self.data_path)

        # Convert Date column to datetime
        self.df['Date'] = pd.to_datetime(self.df['Date'])

        # Calculate missing items
        self.df['Missing Items'] = self.df['Expected Quantity'] - self.df['Actual Quantity']

        # Create time of day classification based on Time column
        def categorize_time(time_str):
            try:
                hour = pd.to_datetime(time_str).hour
                if hour < 12:
                    return 'Morning'
                elif hour < 17:
                    return 'Afternoon'
                else:
                    return 'Evening'
            except:
                return 'Unknown'

        self.df['Time of Day'] = self.df['Time'].apply(categorize_time)

    def create_layout(self):
        """Create the dashboard layout"""
        self.app.layout = html.Div([
            # Title
            html.H1("Store Management Dashboard",
                    style={'textAlign': 'center', 'padding': '20px'}),

            # Filters
            html.Div([
                html.H3("Filters"),
                html.Div([
                    html.Label("Date Range:"),
                    dcc.DatePickerRange(
                        id='date-range',
                        start_date=self.df['Date'].min(),
                        end_date=self.df['Date'].max(),
                        style={'margin': '10px'}
                    ),
                ]),
                html.Div([
                    html.Label("Staff:"),
                    dcc.Dropdown(
                        id='staff-filter',
                        options=[{'label': i, 'value': i}
                                 for i in sorted(self.df['Responsible Staff'].unique())],
                        multi=True,
                        placeholder="Select Staff",
                        style={'margin': '10px'}
                    ),
                ]),
                html.Div([
                    html.Label("Category:"),
                    dcc.Dropdown(
                        id='category-filter',
                        options=[{'label': i, 'value': i}
                                 for i in sorted(self.df['Category'].unique())],
                        multi=True,
                        placeholder="Select Category",
                        style={'margin': '10px'}
                    ),
                ]),
            ], style={'padding': '20px', 'backgroundColor': '#f8f9fa', 'borderRadius': '5px'}),

            # KPIs
            html.Div(id='kpi-display', style={'padding': '20px'}),

            # Charts
            html.Div([
                dcc.Graph(id='missing-items-trend'),
                dcc.Graph(id='category-analysis'),
                dcc.Graph(id='staff-performance'),
                dcc.Graph(id='time-analysis')
            ], style={'padding': '20px'})
        ])

    def create_callbacks(self):
        @self.app.callback(
            [Output('kpi-display', 'children'),
             Output('missing-items-trend', 'figure'),
             Output('category-analysis', 'figure'),
             Output('staff-performance', 'figure'),
             Output('time-analysis', 'figure')],
            [Input('date-range', 'start_date'),
             Input('date-range', 'end_date'),
             Input('staff-filter', 'value'),
             Input('category-filter', 'value')]
        )
        def update_dashboard(start_date, end_date, selected_staff, selected_category):
            # Filter data
            filtered_df = self.df.copy()

            if start_date and end_date:
                filtered_df = filtered_df[
                    (filtered_df['Date'] >= start_date) &
                    (filtered_df['Date'] <= end_date)
                    ]

            if selected_staff:
                filtered_df = filtered_df[
                    filtered_df['Responsible Staff'].isin(selected_staff)
                ]

            if selected_category:
                filtered_df = filtered_df[
                    filtered_df['Category'].isin(selected_category)
                ]

            # Calculate KPIs
            kpis = self.calculate_kpis(filtered_df)

            # Create charts
            trend_fig = self.create_trend_chart(filtered_df)
            category_fig = self.create_category_chart(filtered_df)
            staff_fig = self.create_staff_chart(filtered_df)
            time_fig = self.create_time_chart(filtered_df)

            return kpis, trend_fig, category_fig, staff_fig, time_fig

    def calculate_kpis(self, df):
        total_missing = df['Missing Items'].sum()
        highest_missing_day = df.groupby('Date')['Missing Items'].sum().max()
        worst_category = df.groupby('Category')['Missing Items'].sum().idxmax()
        staff_most_missing = df.groupby('Responsible Staff')['Missing Items'].sum().idxmax()

        return html.Div([
            html.Div([
                html.H4("Key Performance Indicators",
                        style={'textAlign': 'center', 'color': '#2c3e50'}),
                html.Div([
                    html.Div([
                        html.H6("Total Missing Items"),
                        html.H4(f"{int(total_missing):,}")
                    ], className='kpi-box'),
                    html.Div([
                        html.H6("Highest Missing (Single Day)"),
                        html.H4(f"{int(highest_missing_day):,}")
                    ], className='kpi-box'),
                    html.Div([
                        html.H6("Most Affected Category"),
                        html.H4(f"{worst_category}")
                    ], className='kpi-box'),
                    html.Div([
                        html.H6("Staff with Most Missing Items"),
                        html.H4(f"{staff_most_missing}")
                    ], className='kpi-box'),
                ], style={'display': 'flex', 'justifyContent': 'space-around'})
            ])
        ])

    def create_trend_chart(self, df):
        daily_totals = df.groupby('Date')['Missing Items'].sum().reset_index()
        fig = px.line(daily_totals, x='Date', y='Missing Items',
                      title='Missing Items Trend Over Time')
        return fig

    def create_category_chart(self, df):
        category_analysis = df.groupby('Category')['Missing Items'].sum().reset_index()
        fig = px.bar(category_analysis, x='Category', y='Missing Items',
                     title='Missing Items by Category')
        return fig

    def create_staff_chart(self, df):
        staff_analysis = df.groupby('Responsible Staff')['Missing Items'].sum().reset_index()
        fig = px.bar(staff_analysis, x='Responsible Staff', y='Missing Items',
                     title='Missing Items by Staff Member')
        return fig

    def create_time_chart(self, df):
        time_analysis = df.groupby('Time of Day')['Missing Items'].sum().reset_index()
        fig = px.bar(time_analysis, x='Time of Day', y='Missing Items',
                     title='Missing Items by Time of Day')
        return fig

    def run_dashboard(self):
        """Initialize and run the dashboard"""
        self.load_data()
        self.create_layout()
        self.create_callbacks()
        self.app.run_server(debug=True)


# Add some CSS styling
external_stylesheets = [
    {
        'href': 'https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap',
        'rel': 'stylesheet'
    }
]

# Usage
if __name__ == '__main__':
    dashboard = StoreDashboard('C:/Work/EarthlyE/data.xlsx')
    dashboard.run_dashboard()