import streamlit as st
import pandas as pd


st.sidebar.title("Versuch")


df = pd.read_csv("data.csv", sep=";")
#st.write(df)

topic = st.sidebar.selectbox(
    "Topic",
    (df["topic"].unique())
)


topic2 = st.sidebar.selectbox(
    "Sub topic",
    (df[df["topic"]== topic]["sub_topic"].unique())
)

code  = topic2

st.code(code, language='python')


#x = df[df["topic"]== topic]["sub_topic"].unique()

#st.write(x)


#if topic == 
#if topic == "Github":
    #sub_topic = st.sidebar.selectbox(
    #"Thema",
    #("A", "B", "C", "D")
#)

