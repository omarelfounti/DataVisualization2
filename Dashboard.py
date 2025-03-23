import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard():
    df = pd.read_csv("weather_electricity.csv", parse_dates=["Date"])
    st.title("📊 Dashboard")

    show_price_line(df)
    show_temperature_line(df)
    show_wind_bar(df)
    show_humidity_line(df)

def show_price_line(df):
    st.subheader("💰 Electricity Price Over Time (€ / MWh)")
    st.line_chart(df.set_index('Date')["Electricity Price (€/MWh)"])

def show_temperature_line(df):
    st.subheader("🌡️ Temperature Over Time (°C)")
    st.line_chart(df.set_index('Date')["Temperature (°C)"])

def show_wind_bar(df):
    st.subheader("🍃 Wind Speed Over Time (km/h)")
    st.bar_chart(df.set_index('Date')["Wind Speed (km/h)"])

def show_humidity_line(df):
    st.subheader("💧 Humidity Over Time (%)")
    st.line_chart(df.set_index('Date')["Humidity (%)"])




