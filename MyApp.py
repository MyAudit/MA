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

st.header('Аналитический центр - MyAudit')
st.subheader('Комплексная модель автоматизированного поиска рисков нарушений')
st.write('(переход от выборочных проверок к сплошному автоматизированному контролю федерального бюджета)') 


st.write('Доступ ограничен')
password = st.text_input('Для доступа введите пароль:', type='password')
if password != 'Inna':
    st.write('НЕТ ДОСТУПА')
else:
    df = pd.read_excel('https://docs.google.com/spreadsheets/d/1C7UYTDLsPcgmngE45VEH17buU8onkU1q/edit?usp=sharing&ouid=100184939205193698727&rtpof=true&sd=true')
    st.subheader('Анализ ФАИП на 01.10.2023')
    st.write(df)
