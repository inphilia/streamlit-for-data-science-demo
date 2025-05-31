import streamlit as st
import pickle

st.title('Penguin Species Classification')
st.write('''This app uses 6 inputs to predict the species of penguin using
         a model built on the Palmer Penguins dataset. Use the form below
         to get started!''')

with open('random_forest_penguin.pkl', 'rb') as rf_pickle:
    rfc = pickle.load(rf_pickle)
with open('uniques_penguin.pkl', 'rb') as uniques_pickle:
    unique_penguin_mapping = pickle.load(uniques_pickle)
# st.write(rfc)
# st.write(unique_penguin_mapping)

island = st.selectbox('Penguin Island', ['Biscoe', 'Dream', 'Torgersen'])
sex = st.selectbox('Sex', options=['Female', 'Male'])
bill_length = st.number_input('Bill Length (mm)', min_value=0)
bill_depth = st.number_input('Bill Depth (mm)', min_value=0)
flipper_length = st.number_input('Flipper Length (mm)', min_value=0)
body_mass = st.number_input('Body Mass (g)', min_value=0)
# user_inputs = [island, sex, bill_length, bill_depth, flipper_length, body_mass]
# st.write(f'User inputs: {user_inputs}')

island_biscoe, island_dream, island_torgersen = 0, 0, 0
if island == 'Biscoe':
    island_biscoe = 1
elif island == 'Dream':
    island_dream = 1
elif island == 'Torgersen':
    island_torgersen = 1
sex_female, sex_male = 0, 0
if sex == 'Female':
    sex_female = 1
elif sex == 'Male':
    sex_male = 1
new_prediction = rfc.predict([[bill_length, bill_depth, flipper_length, body_mass,
                               island_biscoe, island_dream, island_torgersen,
                               sex_female, sex_male]])
prediction_species = unique_penguin_mapping[new_prediction[0]]
st.write(f'Predicted species: {prediction_species}')
