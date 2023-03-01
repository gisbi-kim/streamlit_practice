import streamlit as st
import altair as alt
import pandas as pd

# Create a DataFrame
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
})

# Create a chart with Altair
chart = alt.Chart(data).mark_line().encode(
    x='x',
    y='y'
).interactive() # enable interactivity


# Display the chart in Streamlit using altair_chart
st.altair_chart(chart)
