import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components

st.set_page_config(page_title="RedBUS",
                   layout= "wide",
                   initial_sidebar_state= "expanded")

hide_streamlit_style = """ <html> <body><h1 style="font-family:Google Sans;font-size:40px"> Red Bus</h1></body>  </html>  """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
Col1,Col2=st.columns(2)
with Col1:
    st.image('./images/about2.png')
    st.image('./images/about3.png')
    st.image('./images/about3.5.png')
with Col2:
    st.image('./images/about4.png')
    st.image('./images/about5.png')
    st.image('./images/about6.png')

hide_streamlit_style = """ <html> <body><h1 style="font-family:Google Sans; color:blue;font-size:40px"> About this Project </h1>
        <p style="font-family:Google Sans; font-size:20px">
        <b>Project_Title</b>: <br>Airbnb Analysis Using Streamlit and Plotly <br>
        <b>Technologies_Used</b> :<br> Python scripting, Data Preprocessing, Visualization,EDA, Streamlit, MongoDb, PowerBI 
        <br>
        <b>Dataset</b>:  <a href="https://drive.google.com/file/d/1C7AilYDf2pA09Jy-5wYysvLwKC9_Fu9X/view?usp=sharing ">Link</a><br>
        <b>Domain </b> : Travel Industry, Property Management and Tourism <br>
        <b>Problem Statement:</b>: <br>
        <b>Author</b> : M.KOBALAN <br>
        <b>Linkedin</b> <a href="https://www.linkedin.com/in/kobalan-m-106267227/ ">Link</a>
        </p>
        </body>  </html>  """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)