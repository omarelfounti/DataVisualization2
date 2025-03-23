import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Dashboard: Daily Trends")

df = pd.read_csv("weather_electricity.csv", parse_dates=['Date'])

st.subheader("Electricity Price Over Time (€ / MWh)")
st.line_chart(df.set_index('Date')["Electricity Price (€/MWh)"])

st.subheader("Temperature Over Time (°C)")
st.line_chart(df.set_index('Date')["Temperature (°C)"])

st.subheader("Wind Speed Over Time (km/h)")
st.bar_chart(df.set_index('Date')["Wind Speed (km/h)"])

