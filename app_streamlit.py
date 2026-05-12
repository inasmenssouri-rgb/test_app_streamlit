import streamlit as st
import time

st.title('suite streamlit')
if st.button('cliquez ici'):
    with st.spinner('chargement en cour...'):
        time.sleep(2)
    st.success('termine !')