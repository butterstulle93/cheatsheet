import streamlit as st
import pandas as pd


st.sidebar.title("Versuch")


df = pd.read_csv("data.csv", sep=";")
#st.write(df)

col1, col2, col3 = st.columns(3)

with col1:
    topic = st.selectbox(
    "Topic",
    (df["topic"].unique()))
    
with col2:
    topic2 = st.selectbox(
    "Sub topic",
    (df[df["topic"]== topic]["sub_topic"].unique())
)

with col3:
    x = df.loc[(df['topic']==topic) & (df['sub_topic']== topic2)]

    y = x["result"].values[0]


    code  = y

    st.code(code, language='python')










