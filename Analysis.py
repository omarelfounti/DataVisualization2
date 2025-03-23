import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show_analysis():
    df = pd.read_csv("weather_electricity.csv", parse_dates=["Date"])
    st.title("📈 Analysis")

    temperature_vs_price(df)
    correlation_heatmap(df)
    weekly_avg_price(df)
    humidity_vs_price(df)

def temperature_vs_price(df):
    st.subheader("🌡️ Temperature vs Electricity Price")
    fig, ax = plt.subplots()
    ax.scatter(df['Temperature (°C)'], df['Electricity Price (€/MWh)'], alpha=0.7)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Electricity Price (€/MWh)")
    st.pyplot(fig)

def correlation_heatmap(df):
    st.subheader("📊 Correlation Heatmap")
    corr = df.drop(columns='Date').corr()
    fig, ax = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

def weekly_avg_price(df):
    st.subheader("📅 Average Weekly Electricity Price")
    df['Week'] = df['Date'].dt.isocalendar().week
    weekly_avg = df.groupby('Week')['Electricity Price (€/MWh)'].mean()

    fig, ax = plt.subplots()
    ax.plot(weekly_avg.index, weekly_avg.values, marker='o')
    ax.set_xlabel("Week Number")
    ax.set_ylabel("Average Price (€ / MWh)")
    ax.set_title("Weekly Average Electricity Price")
    st.pyplot(fig)

def humidity_vs_price(df):
    st.subheader("💧 Humidity vs Electricity Price")
    fig, ax = plt.subplots()
    ax.scatter(df['Humidity (%)'], df['Electricity Price (€/MWh)'], color='green', alpha=0.6)
    ax.set_xlabel("Humidity (%)")
    ax.set_ylabel("Electricity Price (€/MWh)")
    st.pyplot(fig)


