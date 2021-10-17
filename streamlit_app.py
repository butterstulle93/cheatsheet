import streamlit as st
import pandas as pd


st.sidebar.title("Versuch")


topic = st.sidebar.selectbox(
    "Unter Thema",
    ("Github", "Latex", "Pandas", "Python")
)

if topic == "Github":
    sub_topic = st.sidebar.selectbox(
    "Thema",
    ("A", "B", "C", "D")
)


df = pd.read_csv("data.csv", sep=";")
st.write(df)