

# C:\Users\User>cd C:\Users\User\Documents\IDE_Github
# C:\Users\User\Documents\АЦСПРФ>streamlit run MyApp.py
 
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

st.header('Аналитический портал')
# st.subheader('Комплексная модель автоматизированного поиска рисков нарушений')
# st.write('(переход от выборочных проверок к сплошному автоматизированному контролю федерального бюджета)') 


# st.write('Доступ ограничен')
password = st.text_input('Для доступа введите пароль:', type='password')
if password != 'Inna':
    st.write('НЕТ ДОСТУПА')
else:
    gsheet = st.sidebar.checkbox('gsheet прямо')
    if gsheet:
        st.subheader('Анализ gsheet прямо')
        # df = pd.read_excel('https://docs.google.com/spreadsheets/d/1C7UYTDLsPcgmngE45VEH17buU8onkU1q/edit?usp=sharing&ouid=100184939205193698727&rtpof=true&sd=true')
        df = pd.read_excel('https://docs.google.com/spreadsheets/d/1C7UYTDLsPcgmngE45VEH17buU8onkU1q/export?format=csv&gid=1017825111')
        st.write(df)
        
        
    gsheet = st.sidebar.checkbox('gsheet через git')
    if gsheet:
        st.subheader('Анализ gsheet через git')
        # df = pd.read_excel('https://docs.google.com/spreadsheets/d/1C7UYTDLsPcgmngE45VEH17buU8onkU1q/edit?usp=sharing&ouid=100184939205193698727&rtpof=true&sd=true')
        df = pd.read_excel('https://docs.google.com/spreadsheets/d/1C7UYTDLsPcgmngE45VEH17buU8onkU1q/export?format=csv&gid=1017825111')
        st.write(df)
    
    git = st.sidebar.checkbox('git файл и папки')
    if git:
        st.subheader('Анализ git файл и папки')
        df = pd.read_excel('https://github.com/MyAudit/MA/raw/master/!%202023%2010%2001%20faip_sravnenie_k%202023%2010%2025_1.xlsx')
        st.write(df)
    
   


