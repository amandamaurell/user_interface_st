import requests
import streamlit as st

query = st.text_input("Sreach for a GIF")

url = "https://api.giphy.com/v1/gifs/search"
params = {'api_key':st.secrets.api_key, "q":query}
response = requests.get(url, params=params).json()

st.write(f"<iframe src={response['data'][0]['embed_url']}>", unsafe_allow_html=True)
