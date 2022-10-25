import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('California Housing Data (1990) by Haotian Lan')

df = pd.read_csv('housing.csv')

pop_filter = st.slider('Median House Price', 0, 500001, 200000)
df = df[df.median_house_value >= pop_filter]

location = df.ocean_proximity.unique()
location_filter = st.sidebar.multiselect('Choose the location type', location, location)
df = df[df.ocean_proximity.isin(location_filter)]

income_level = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

if income_level == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5 )]
else:
    df = df[df.median_income > 4.5]

st.subheader('See more filters in the sidebar:')
st.map(df)

st.subheader('Histogram of the Median House Value:')
fig, ax = plt.subplots()
pop_median_house_value = df.median_house_value.hist(bins=30)
st.pyplot(fig)