import streamlit as st
from Dashboard import show_dashboard
from Analysis import show_analysis

st.sidebar.title("Options")
option = st.sidebar.selectbox("Choose a page", ["Home", "Dashboard", "Analysis"])

if option == "Dashboard":
    show_dashboard()
elif option == "Analysis":
    show_analysis()
else:
    st.title("🌦️ Weather vs Electricity Prices")
    st.write("Welcome to the app! Choose a section from the menu below:")




