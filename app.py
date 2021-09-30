import streamlit as st
import pandas as pd

st.title("Cheat Sheet")


add_selectbox = st.sidebar.selectbox(
    "Thema",
    ("Github", "Latex", "Pandas", "Python")
)