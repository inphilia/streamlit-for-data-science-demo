import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_plotly_events import plotly_events

st.title("Streamlit Plotly Events Example: Penguins")
df = pd.read_csv("penguins.csv")

fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="species")
# st.plotly_chart(fig)
selected_point = plotly_events(fig, click_event=True)
st.write('Selected point:')
st.write(selected_point)

# df = px.data.iris()
# fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# selected_points = plotly_events(fig, click_event=True)

# if selected_points:
#     st.write("Selected Points:", selected_points)
#     for point in selected_points:
#         st.write(f"Species: {df['species'][point['pointIndex']]}, Sepal Width: {df['sepal_width'][point['pointIndex']]}, Sepal Length: {df['sepal_length'][point['pointIndex']]}")