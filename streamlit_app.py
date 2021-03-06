import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")




df = pd.read_csv("data.csv", sep=";")
#st.write(df)

col1, col2 = st.columns(2)


with col1:
    st.title("Explorer")
    topic = st.selectbox(
    "Topic",
    (df["topic"].unique()),      )
    
    if topic != 0:
        topic2 = st.selectbox(
        "Sub topic",
        (df[df["topic"]== topic]["sub_topic"].unique())

        )
with col2:
    x = df.loc[(df['topic']==topic) & (df['sub_topic']== topic2)]
    y = x["result"].values[0]
    code  = y

    if topic == "Latex":
        platz = "latex"
    else:
        platz = "code"
        

    st.title("Code")
    st.platz(code, language='python')

    #st.title("Note")
    #st.code(code, language='python')










