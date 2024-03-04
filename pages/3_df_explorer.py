from streamlit_extras.dataframe_explorer import dataframe_explorer
import pandas as pd
import streamlit as st

data_url = "https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv"


df = pd.read_csv(data_url)
filtered_df = dataframe_explorer(df, case=False)
st.dataframe(filtered_df, use_container_width=True)
