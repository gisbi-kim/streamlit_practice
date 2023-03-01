import streamlit as st
import altair as alt
import pandas as pd
import math 
import time

sun_radius = 696340  # km
earth_radius = 63710  # km
distance = 149.6e6  # km

# Compute position of Sun
sun_x = 0
sun_y = 0

# Create initial DataFrame for Earth
earth_angle = 0.0
earth_x = distance * math.cos(earth_angle)
earth_y = distance * math.sin(earth_angle)
data = pd.DataFrame({
    'x': [earth_x],
    'y': [earth_y],
    'radius': [earth_radius],
    'color': ['blue']
})

# Create initial chart
chart = alt.Chart(data).mark_circle().encode(
    x='x',
    y='y',
    size='radius',
    color='color',
    tooltip=[alt.Tooltip('radius', title='Radius (km)')]
).properties(
    width=600,
    height=600
)

# Show the initial chart
chart_view = st.altair_chart(chart)

# Animate the Earth's orbit
while True:
    # Update Earth's position
    earth_angle += 0.1
    earth_x = distance * math.cos(earth_angle)
    earth_y = distance * math.sin(earth_angle)
    
    # Update DataFrame
    data = pd.DataFrame({
        'x': [earth_x, sun_x],
        'y': [earth_y, sun_y],
        'radius': [earth_radius, sun_radius],
        'color': ['blue', 'red']
    })
    
    # Update chart in-place
    chart = alt.Chart(data).mark_circle().encode(
        x='x',
        y='y',
        size='radius',
        color='color',
        tooltip=[alt.Tooltip('radius', title='Radius (km)')]
    ).properties(
        width=600,
        height=600,
    )
    chart_view.altair_chart(chart)
    
    # Pause for a short time to control animation speed
    time.sleep(1.0)
