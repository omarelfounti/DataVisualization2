import streamlit as st
from Analysis import show_analysis
from Dashboard import show_dashboard

st.title("🌦️ Weather vs Electricity Prices")
st.write("Welcome to the app! Choose a section from the menu below:")

page = st.selectbox("Select a page", ["Home", "Dashboard", "Analysis"])

if page == "Dashboard":
    show_dashboard()
elif page == "Analysis":
    show_analysis()
else:
    st.write("""
        This tool helps you understand how temperature, wind speed, and humidity 
        relate to electricity prices using a fictional dataset for one month.
    """)


