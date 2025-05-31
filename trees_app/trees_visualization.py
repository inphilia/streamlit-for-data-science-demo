import streamlit as st
import pandas as pd
# import plotly.express as px
# import matplotlib.pyplot as plt
# import seaborn as sns
# import datetime as dt
# from bokeh.plotting import figure
# from streamlit_bokeh import streamlit_bokeh
import altair as alt
import pydeck as pdk

# %% Set up the page

st.title('SF Trees')
st.write(
    '''This app analyzes trees in San Francisco using
    a dataset kindly provided by SF DPW (Department of Public Works).'''
)
st.subheader('Plotly Chart')

# %% Process the data

trees_df = pd.read_csv('trees.csv')

# # plotly
# st.subheader('Plotly Chart')
# fig = px.histogram(trees_df['dbh'])
# st.plotly_chart(fig)

# # seaborn and matplotlib
# trees_df['age'] = (pd.to_datetime('today') - pd.to_datetime(trees_df['date'])).dt.days
# st.subheader('Seaborn Chart')
# fig_sb, ax_sb = plt.subplots()
# ax_sb = sns.histplot(trees_df['age'])
# plt.xlabel('Age (Days)')
# st.pyplot(fig_sb)
# st.subheader('Matplotlib Chart')
# fig_mpl, ax_mpl = plt.subplots()
# ax_mpl = plt.hist(trees_df['age'])
# plt.xlabel('Age (Days)')
# st.pyplot(fig_mpl)

# # bokeh
# st.subheader('Bokeh Chart')
# scatterplot = figure(title = 'Bokeh Scatter Plot')
# scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
# scatterplot.yaxis.axis_label = 'Site Order'
# scatterplot.xaxis.axis_label = 'DBH'
# streamlit_bokeh(scatterplot)

# # altair
# st.subheader('Altair Chart')
# # df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
# # df_caretaker.columns = ['caretaker', 'tree_count']
# # fig = alt.Chart(df_caretaker).mark_bar().encode(x = 'caretaker', y = 'tree_count')
# # st.altair_chart(fig)
# fig = alt.Chart(trees_df).mark_bar().encode(x = 'caretaker', y = 'count(*):Q')
# st.altair_chart(fig)

# PyDeck which uses Mapbox
trees_df = trees_df.dropna(how='any', inplace=False)
st.subheader('PyDeck Map')
sf_initial_view = pdk.ViewState(
    latitude=37.77,
    longitude=-122.4,
    zoom=11,
    pitch=30
)
# sp_layer = pdk.Layer(
#     'ScatterplotLayer',
#     data = trees_df,
#     get_position = ['longitude', 'latitude'],
#     get_radius = 30
# )
hx_layer = pdk.Layer(
    'HexagonLayer',
    data = trees_df,
    get_position = ['longitude', 'latitude'],
    radius = 100,
    extruded = True
)
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=sf_initial_view,
    # layers = [sp_layer]
    layers = [hx_layer]
    ))

# %% Notes

# view streamlit settings
# streamlit config show

# configure mapbox token
# code /.streamlit/config.toml
# [mapbox]
# token = "123my_large_mapbox_token456"
# or set it in terminal
# streamlit config set mapbox.token <your_mapbox_token>

