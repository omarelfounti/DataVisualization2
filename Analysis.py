import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🔍 Analysis: Correlations & Insights")

df = pd.read_csv("weather_electricity.csv", parse_dates=['Date'])

st.subheader("Scatter: Temperature vs Electricity Price")
fig, ax = plt.subplots()
ax.scatter(df['Temperature (°C)'], df['Electricity Price (€/MWh)'], alpha=0.7)
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Electricity Price (€/MWh)")
st.pyplot(fig)

st.subheader("Heatmap of Correlation Between Variables")
corr = df.drop(columns=['Date']).corr()
fig2, ax2 = plt.subplots()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax2)
st.pyplot(fig2)

st.subheader("Average Weekly Electricity Price")
df['Week'] = df['Date'].dt.isocalendar().week
weekly_avg = df.groupby('Week')['Electricity Price (€/MWh)'].mean()
st.bar_chart(weekly_avg)
