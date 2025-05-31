import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

penguin_df = pd.read_csv('penguins.csv')
# print(penguin_df.head())
penguin_df = penguin_df.dropna(inplace=False)
output = penguin_df['species']
features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm', 
                       'flipper_length_mm', 'body_mass_g', 'sex']]
features = pd.get_dummies(features)
output, uniques = pd.factorize(output) #convert strings to integers
x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=0.8)
rfc = RandomForestClassifier(random_state=42)
rfc.fit(x_train.values, y_train)
y_pred = rfc.predict(x_test.values)
score = accuracy_score(y_pred, y_test)
print(f'Accuracy score: {score:.2f}')

# print('Here are our output variables')
# print(output.head())
# print('Here are our feature variables')
# print(features.head())

# Save the model
with open('random_forest_penguin.pkl', 'wb') as f:
    pickle.dump(rfc, f)
with open('uniques_penguin.pkl', 'wb') as f:
    pickle.dump(uniques, f)

fig, ax = plt.subplots()
ax = sns.barplot(x=rfc.feature_importances_, y=features.columns)
plt.title('Feature Importances for species prediction')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.tight_layout()
fig.savefig('feature_importances.png')
