import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Data Dashboard-Elliott')

DATA_URL = ('sales_data.csv')
def load_data():
  data = pd.read_csv(DATA_URL)
  return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data...done!')


if st.checkbox('Show raw data'):
  st.subheader('Raw data')
  st.write(data)

st.subheader('Number of Sales by product')
hist_values = np.histogram(
  data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)


