import penguin
import penguin1
import firstpage
import streamlit as st
PAGES = {
    "Home Page":firstpage,
    "Image Classification": penguin,
    "Data Prediction": penguin1,
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
