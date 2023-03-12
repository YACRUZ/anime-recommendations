import streamlit as st 
import pandas as pd 

st.title('Anime recommendations')
DATA_URL = ('anime.csv')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data   

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Done ! using cache...')

st.dataframe(data)