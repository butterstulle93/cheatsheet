import streamlit as st
import pandas as pd





df = pd.read_csv("data.csv", sep=";")
#st.write(df)

col1, col2 = st.columns(2)

with col1:
    topic = st.selectbox(
    "Topic",
    (df["topic"].unique()),  int = 0)
    
    if topic != 0:
        topic2 = st.selectbox(
        "Sub topic",
        (df[df["topic"]== topic]["sub_topic"].unique())

        )
with col2:
    x = df.loc[(df['topic']==topic) & (df['sub_topic']== topic2)]
    y = x["result"].values[0]
    code  = y
    st.code(code, language='python')










