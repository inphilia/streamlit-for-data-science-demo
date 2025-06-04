import pandas as pd
import plotly.express as px
import requests
import streamlit as st
# from pandas_profiling import ProfileReport
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from streamlit_lottie import st_lottie
from streamlit_plotly_events import plotly_events

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_penguin = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json')
st_lottie(lottie_penguin, height=200, speed=1.5)

st.title("Streamlit Plotly Events + Lottie Example: Penguins")
df = pd.read_csv("penguins.csv")

fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", color="species")
st.plotly_chart(fig)
# selected_point = plotly_events(fig, click_event=True)
# st.write('Selected point:')
# st.write(selected_point)

st.subheader('Pandas Profiling of Penguin Dataset')
penguin_profile = ProfileReport(df, explorative=True)
st_profile_report(penguin_profile)
