import streamlit as st
import pandas as pd

st.title("This is my World")
show_home =st.sidebar.button("Home")
show_dashboard = st.sidebar.button("Dashboard")

if show_dashboard:
    st.title("👪 My Family Detail")
    st.sidebar.header("Upload Your CSV File")
    file = st.sidebar.file_uploader("Upload CSV", type=["csv"])
    df = pd.DataFrame(
                         {
                            'Name': ["Uday","Seema","Sagar","Shekhar","Rupali","Vanya"],
                            'Age': [58, 46, 31,28,26,1]
                        }
                    )
    df
    st.image("sagar.jpg")


Show_contact=st.sidebar.button("contact Us")
if Show_contact:
    st.header("Contact Detail:")
    st.header("call sagar on below number")
    st.header("Call me on :- 9060240503")




Show_about=st.sidebar.button("About Us")
if Show_about:
    st.title("Detail About Out Organization:")
    st.header("Software Power Hub")
    st.chat_message("ai")
    st.image("father.jpg")

