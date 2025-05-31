import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns
import time

# %% App to visualize penguin data using Streamlit

st.title("Palmer's Penguins")
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')

# %% Load the penguin dataset

penguin_file = st.file_uploader('Select Your Local Penguins CSV (default provided)')
@st.cache_data()
def load_file(penguin_file):
    time.sleep(3)
    if penguin_file is not None:
        penguins_df = pd.read_csv(penguin_file)
    else:
        penguins_df = pd.read_csv('penguins.csv')
        # st.stop()
    return penguins_df
penguins_df = load_file(penguin_file)

# %% User input for filtering the dataset

# selected_species = st.selectbox('What species would you like to visualize?', [
#                                 'Adelie', 'Gentoo', 'Chinstrap'])
# penguins_df_filtered = penguins_df[penguins_df['species'] == selected_species]
selected_x_var = st.selectbox('What do you want the x variable to be?',
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y variable?',
                              ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_gender = st.selectbox('What gender do you want to filter for?',
                               ['all penguins', 'male', 'female'])
if selected_gender == 'male':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass

# %% Plotting the scatterplot using Altair

sns.set_style('darkgrid')
markers = {'Adelie': 'X', 'Gentoo': 's', 'Chinstrap': 'o'}
alt_chart = (
    alt.Chart(penguins_df, title=f"Scatterplot of Palmer's Penguins").mark_circle().encode(
        x=selected_x_var,
        y=selected_y_var,
        color='species',
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)

# %% Old Code

# st.write(penguins_df.head())
