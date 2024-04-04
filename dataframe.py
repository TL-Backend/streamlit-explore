import streamlit as st
import pandas as pd
import numpy as np

def basic_table():
  st.markdown("**<u>Basic Table Using Pandas</u>**", unsafe_allow_html=True)
  data = {
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40],
  'third column': [1,2,3,4]
  }
  df = pd.DataFrame(data)
  # st.dataframe(df.style.highlight_max(axis=1)) #will highlight some cells
  st.table(df)  #fixed blocks
  # st.write(df)  #adjustable blocks - allows download csv, search

def numpy_random_table():
  st.markdown("**<u>Numpy for Random numbers</u>**", unsafe_allow_html=True)
  data = np.random.randn(10, 3)  
  st.table(data)


