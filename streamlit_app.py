import streamlit as st
import pandas as pd


st.sidebar.title("Versuch")


df = pd.read_csv("data.csv", sep=";")
#st.write(df)

topic = st.sidebar.selectbox(
    "Unter Thema",
    (df["topic"].unique)
)

#if topic == "Github":
    #sub_topic = st.sidebar.selectbox(
    #"Thema",
    #("A", "B", "C", "D")
#)

