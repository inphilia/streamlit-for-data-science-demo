import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title('Penguin Species Classification')
st.write('''This app uses 6 inputs to predict the species of penguin using
         a model built on the Palmer Penguins dataset. Use the form below
         to get started!''')
password_guess = st.text_input('What is the password to use this app?',
                              type='password',
                              placeholder='Enter password here')
# set secret in streamlit, settings, secrets
if password_guess != st.secrets['password']:
    st.error('Incorrect password. Please try again.')
    st.stop()

penguin_file = st.file_uploader('Upload your own penguin data')
if penguin_file is None:
    penguin_df = pd.read_csv('penguins.csv')
    penguin_df = penguin_df.dropna(inplace=False)
    with open('random_forest_penguin.pkl', 'rb') as rf_pickle:
        rfc = pickle.load(rf_pickle)
    with open('uniques_penguin.pkl', 'rb') as uniques_pickle:
        unique_penguin_mapping = pickle.load(uniques_pickle)
else:
    penguin_df = pd.read_csv(penguin_file)
    penguin_df = penguin_df.dropna(inplace=False)
    output = penguin_df['species']
    features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm', 
                        'flipper_length_mm', 'body_mass_g', 'sex']]
    features = pd.get_dummies(features)
    output, unique_penguin_mapping = pd.factorize(output) #convert strings to integers
    x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=0.8)
    rfc = RandomForestClassifier(random_state=42)
    rfc.fit(x_train.values, y_train)
    y_pred = rfc.predict(x_test.values)
    score = accuracy_score(y_pred, y_test)
    st.write(f'We trained a model on the data with an accuracy score of {score:.2f}!')
st.write('Use the inputs below to try out the model.')

with st.form('user_inputs'):
    island = st.selectbox('Penguin Island', ['Biscoe', 'Dream', 'Torgersen'])
    sex = st.selectbox('Sex', options=['Female', 'Male'])
    bill_length = st.number_input('Bill Length (mm)', min_value=0, value=40)
    bill_depth = st.number_input('Bill Depth (mm)', min_value=0, value=18)
    flipper_length = st.number_input('Flipper Length (mm)', min_value=0, step=5, value=200)
    body_mass = st.number_input('Body Mass (g)', min_value=0)
    st.form_submit_button('Predict Species')
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

st.subheader("Predicting Your Penguin's Species:")
st.write(f'We predict the species to be: {prediction_species}')
st.write('The features used in this prediction are ranked by relative importance below.')
st.image('feature_importances.png')

st.write('Below are the histograms for each continuous variable separated by penguin species. The vertical line represents your inputted value.')
# bill length
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['bill_length_mm'],
                 hue=penguin_df['species'])
plt.axvline(bill_length)
plt.title('Bill Length by Species')
st.pyplot(ax)
# bill depth
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['bill_depth_mm'],
                 hue=penguin_df['species'])
plt.axvline(bill_depth)
plt.title('Bill Depth by Species')
st.pyplot(ax)
# flipper length
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df['flipper_length_mm'],
                 hue=penguin_df['species'])
plt.axvline(flipper_length)
plt.title('Flipper Length by Species')
st.pyplot(ax)