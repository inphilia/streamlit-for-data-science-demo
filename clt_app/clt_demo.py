import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# %% This is a simple app to demonstrate the Central Limit Theorem (CLT)

st.title('Central Limit Theorem with Streamlit')
st.subheader('An App by Alan Nam')
st.write(('This app demonstrates the Central Limit Theorem (CLT) by simulating a '
          'binomial distribution of coin flips and plotting the distribution of means.'))
perc_heads = st.number_input(label = 'Chance of Coins Landing Heads',
                             min_value=0.0, max_value=1.0, value=0.5, step=0.01)
graph_title = st.text_input(label='Graph Title', value='Distribution of Means')
binom_dist = np.random.binomial(n=1, p=perc_heads, size=1000)
list_of_means = [np.random.choice(binom_dist, size=100, replace=True).mean() for _ in range(1000)]

# %% plotting the distribution of means

fig, ax = plt.subplots()
plt.hist(list_of_means, bins='rice')
plt.title(graph_title)
st.pyplot(fig)

# fig, ax = plt.subplots()
# ax = plt.hist(list_of_means, bins='rice')
# st.pyplot(fig)

# st.write(np.mean(binom_dist))
# st.write('Hello World!')


# %% We can call st.pyplot() cirectly without specifying ax but that is not recommended

# plt.hist(list_of_means)
# st.pyplot()
# plt.hist([1,1,1,1])
# st.pyplot()

# This will plot a single histogram with all data

# To do it properly, we want to create each graph explicitly
# fig1, ax1 = plt.subplots()
# ax1 = plt.hist(list_of_means, bins='rice')
# st.pyplot(fig1)

# fig2, ax2 = plt.subplots()
# ax2 = plt.hist([1, 1, 1, 1])
# st.pyplot(fig2)
