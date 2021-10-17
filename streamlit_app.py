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




#df.loc[(df['Salary_in_1000']>=100) & (df['Age']< 60) & (df['FT_Team'].str.startswith('S')),['Name','FT_Team']]

x = df.loc[(df['topic']==topic) & (df['sub_topic']== topic2)]

y = x["result"].values[]


code  = y

st.code(code, language='python')


#x = df[df["topic"]== topic]["sub_topic"].unique()

#st.write(x)


#if topic == 
#if topic == "Github":
    #sub_topic = st.sidebar.selectbox(
    #"Thema",
    #("A", "B", "C", "D")
#)

