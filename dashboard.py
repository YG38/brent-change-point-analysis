import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Brent Oil Price Analysis",
    page_icon="🛢️",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    data_dir = Path("./data")
    prices_df = pd.read_csv(data_dir / "raw/BrentOilPrices.csv", parse_dates=['Date'], dayfirst=True)
    events_df = pd.read_csv(data_dir / "raw/events_tabdata.csv", parse_dates=['event_date'])
    return prices_df, events_df

prices_df, events_df = load_data()

# Sidebar
st.sidebar.title("Dashboard Controls")
st.sidebar.markdown("### Date Range")
min_date = prices_df['Date'].min()
max_date = prices_df['Date'].max()
start_date = st.sidebar.date_input("Start date", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End date", max_date, min_value=min_date, max_value=max_date)

# Filter data
filtered_prices = prices_df[(prices_df['Date'] >= pd.to_datetime(start_date)) & 
                           (prices_df['Date'] <= pd.to_datetime(end_date))]

# Main content
st.title("Brent Oil Price Analysis Dashboard")

# Price trend
st.header("Price Trend")
fig = px.line(filtered_prices, x='Date', y='Price', 
              title="Brent Crude Oil Prices Over Time",
              labels={"Price": "Price (USD/barrel)", "Date": "Date"})

# Add event markers
for _, event in events_df.iterrows():
    fig.add_vline(x=event['event_date'], line_dash="dash", line_color="red", 
                 opacity=0.3, name=event['event_name'])
    
st.plotly_chart(fig, use_container_width=True)

# Event impact analysis
st.header("Event Impact Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Key Events")
    st.dataframe(events_df[['event_date', 'event_name', 'expected_impact']])

with col2:
    st.subheader("Impact Summary")
    impact_stats = events_df.groupby('impact_direction').size().reset_index(name='count')
    fig_pie = px.pie(impact_stats, values='count', names='impact_direction', 
                     title="Impact Direction Distribution")
    st.plotly_chart(fig_pie, use_container_width=True)

# Data table
expander = st.expander("View Raw Data")
with expander:
    st.dataframe(filtered_prices)

# Footer
st.markdown("---")
st.markdown("### About")
st.markdown("""
This dashboard provides an interactive visualization of Brent crude oil prices and their correlation with major global events.

**Data Source**: Historical Brent crude oil prices (1987-2022)

**Methodology**: Bayesian change point detection and time series analysis
""")
