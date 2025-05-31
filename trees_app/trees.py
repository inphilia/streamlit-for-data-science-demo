import streamlit as st
import pandas as pd
import numpy as np

# %% Set up the page

st.title('SF Trees')
st.write(
    '''This app analyzes trees in San Francisco using
    a dataset kindly provided by SF DPW (Department of Public Works).'''
)

# %% Process the data

trees_df = pd.read_csv('trees.csv')
# st.write(trees_df.head())

# version 1 using default
# df_dbh_grouped = pd.DataFrame(trees_df.groupby('dbh').count()['tree_id'])
# df_dbh_grouped.columns = ['tree_count']
# st.line_chart(df_dbh_grouped)
# df_dbh_grouped['new_col'] = np.random.randn(len(df_dbh_grouped)) * 500
# st.line_chart(df_dbh_grouped)
# st.bar_chart(df_dbh_grouped)
# st.area_chart(df_dbh_grouped)

# # version 2 
# df_dbh_grouped = pd.DataFrame(trees_df.groupby('dbh').count()['tree_id']).reset_index()
# df_dbh_grouped.columns = ['dbh', 'tree_count']
# st.line_chart(df_dbh_grouped, x='dbh', y='tree_count')

# Verion 3 map
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000)
st.map(trees_df)

# %% Notes

# streamlit default uses Altair
# st.line_chart()
# st.bar_chart()
# st.area_chart()

# PyDeck
# st.map()


