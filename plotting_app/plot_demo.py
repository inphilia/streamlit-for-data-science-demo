import streamlit as st
import time
import numpy as np

progress_bar = st.sidebar.progress(0, text="Initializing...")
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows, use_container_width=True)
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text('%i%% Complete' % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)
progress_bar.empty()
st.button('Re-run')
# Virtual environment: .\streamlit-env\Scripts\activate
# run with: streamlit run plotting_app/plot_demo.py
