import streamlit as st
import pandas as pd

def show_dashboard():
    st.title("📊 Dashboard")
    df = pd.read_csv("weather_electricity.csv", parse_dates=["Date"])
    st.line_chart(df.set_index("Date")["Electricity Price (€/MWh)"])



