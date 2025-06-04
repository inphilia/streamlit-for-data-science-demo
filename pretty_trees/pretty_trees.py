import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide', page_title='SF Trees Visualization')
st.title('SF Trees')
st.write(
    '''This app analyzes trees in San Francisco using
    a dataset kindly provided by SF DPW (Department of Public Works).'''
)
trees_df = pd.read_csv('trees.csv')
today = pd.to_datetime('today')
trees_df['date'] = pd.to_datetime(trees_df['date'])
trees_df['age'] = (today - trees_df['date']).dt.days
unique_caretakers = trees_df['caretaker'].unique()
owners = st.sidebar.multiselect('Tree Owner Filter', unique_caretakers)
graph_color = st.sidebar.color_picker('Graph Colors', value='#3CF769')
if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]
df_dbh_grouped = pd.DataFrame(trees_df.groupby('dbh').count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

col1, col2 = st.columns(2)
with col1:
    fig = px.histogram(trees_df, x=trees_df['dbh'], title='Tree Width', color_discrete_sequence=[graph_color])
    fig.update_xaxes(title_text='Width')
    st.plotly_chart(fig)
with col2:
    fig = px.histogram(trees_df, x=trees_df['age'], title='Tree Age', color_discrete_sequence=[graph_color])
    st.plotly_chart(fig)

# st.write('Trees by Location')
# trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
# trees_df = trees_df.sample(n=1000, replace=True)
# st.map(trees_df)

# st.line_chart(df_dbh_grouped)
# trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
# trees_df = trees_df.sample(n=1000, replace=True)
# st.map(trees_df)

# tab1, tab2, tab3 = st.tabs(['Line Chart', 'Bar Chart', 'Area Chart'])
# with tab1:
#     st.line_chart(df_dbh_grouped)
# with tab2:
#     st.bar_chart(df_dbh_grouped)
# with tab3:
#     st.area_chart(df_dbh_grouped)

# col1, col2, col3 = st.columns(3, gap='large')
# with col1:
#     st.line_chart(df_dbh_grouped, use_container_width=False)
# with col2:
#     st.bar_chart(df_dbh_grouped)
# with col3:
#     st.area_chart(df_dbh_grouped)

# %% User determined column widths

# first_width = st.number_input('First column width', min_value=1, value=1, step=1)
# second_width = st.number_input('Second column width', min_value=1, value=1, step=1)
# third_width = st.number_input('Third column width', min_value=1, value=1, step=1)

# col1, col2, col3 = st.columns((first_width, second_width, third_width))
# with col1:
#     st.write('Column 1')
# with col2:
#     st.write('Column 2')
# with col3:
#     st.write('Column 3')
