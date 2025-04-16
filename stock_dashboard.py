import streamlit as st
import plotly.graph_objects as go
from stock_analysis import fetch_stock_data, calculate_moving_averages

# Streamlit App Title
st.title("Interactive Stock Market Dashboard")

# Input for the stock symbol
symbol = st.text_input("Enter Stock Symbol", "AAPL")

# Fetch the data for the given symbol
data = fetch_stock_data(symbol)

if data is not None:
    # Calculate moving averages
    data = calculate_moving_averages(data)

    # Plot the data using Plotly
    fig = go.Figure()

    # Add stock closing prices
    fig.add_trace(go.Scatter(x=data.index, y=data['4. close'], mode='lines', name='Close Price', line=dict(color='blue')))

    # Add 50-day moving average
    fig.add_trace(go.Scatter(x=data.index, y=data['50_MA'], mode='lines', name='50-Day MA', line=dict(color='red')))

    # Add 200-day moving average
    fig.add_trace(go.Scatter(x=data.index, y=data['200_MA'], mode='lines', name='200-Day MA', line=dict(color='green')))

    # Layout customization
    fig.update_layout(title=f'{symbol} Stock Price with Moving Averages',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      template='plotly_dark')

    # Display the chart in the app
    st.plotly_chart(fig)

else:
    st.error(f"Unable to retrieve data for {symbol}. Please try again.")
