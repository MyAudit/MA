#  You can now view your Streamlit app in your browser.

#  Local URL: http://localhost:8501
#  Network URL: http://192.168.34.152:8501
  
# РАЗВОРАЧИВАЕМ СТРИМЛИТ-
import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="MyAudit",
    layout="wide"
)

st.write("""
         # NEW - Электронный бюджет 
         Аналитическая часть *для инспекторов*
         """)

password = st.text_input('Для доступа введите пароль:')
if password != 'inna':
    st.write('Нет доступа')
else:
    df = pd.DataFrame({'ГРБС':['056','149','388'],'Вид расходов':[500,600,400],'БА':[10000.0,20000.0,30000.0]})
    st.write(df)
