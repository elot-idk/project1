import streamlit as st
import pandas as pd
import numpy as np

st.title('Simple Data Dashboard-Elliott')

DATA_URL = ()
def load_data():
  data = pd.read_csv(DATA_URL)
  return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data...done!')


