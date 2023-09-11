<<<<<<< HEAD
# 1) СОЗДАНИЕ VSCODE И РАЗМЕЩЕНИЕ В STREAMLIT
# Streamlit с инструкцией по деплою, который применен ниже в этой программе
# https://streamlit.io/

# 2) Видео пример как деплоить из ютуба
# https://www.youtube.com/watch?v=0kLJ43KATb0

# 3) ОБРАБОТКА В GIT
# https://streamlit.io/cloud


#  Warning: to view this Streamlit app on a browser, run it with the following
#  command:

#    streamlit run streamlit run c:/Users/User/Documents/IDE/MyApp.py
# >> [ARGUMENTS]er>

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
         # NEW! Электронный бюджет
         Аналитическая часть *для инспекторов*
         """)

df = pd.DataFrame({'ГРБС':['056','149','388'],'Вид расходов':[500,600,400],'БА':[10000.0,20000.0,30000.0]})
st.write(df)


# появляется команда которую надо скопировать и запустить здесь же в терминале
# после чего появляется хост

#  Warning: to view this Streamlit app on a browser, run it with the following
#  command:

#    streamlit run streamlit run c:/Users/User/Documents/IDE/MyApp.py
# >> [ARGUMENTS]er>

#  You can now view your Streamlit app in your browser.

#  Local URL: http://localhost:8501
#  Network URL: http://192.168.34.152:8501



# ПОПЫТКА ЗАКОММИТИТЬ

=======
# 1) СОЗДАНИЕ VSCODE И РАЗМЕЩЕНИЕ В STREAMLIT
# Streamlit с инструкцией по деплою, который применен ниже в этой программе
# https://streamlit.io/

# 2) Видео пример как деплоить из ютуба
# https://www.youtube.com/watch?v=0kLJ43KATb0

# 3) ОБРАБОТКА В GIT
# https://streamlit.io/cloud


#  Warning: to view this Streamlit app on a browser, run it with the following
#  command:

#    streamlit run streamlit run c:/Users/User/Documents/IDE/MyApp.py
# >> [ARGUMENTS]er>

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
         # Электронный бюджет
         Аналитическая часть *для инспекторов*
         """)

df = pd.DataFrame({'ГРБС':['056','149','388'],'Вид расходов':[500,600,400],'БА':[10000.0,20000.0,30000.0]})
st.write(df)


# появляется команда которую надо скопировать и запустить здесь же в терминале
# после чего появляется хост

#  Warning: to view this Streamlit app on a browser, run it with the following
#  command:

#    streamlit run streamlit run c:/Users/User/Documents/IDE/MyApp.py
# >> [ARGUMENTS]er>

#  You can now view your Streamlit app in your browser.

#  Local URL: http://localhost:8501
#  Network URL: http://192.168.34.152:8501
>>>>>>> d92014ceff4c1c5f2f3b7f9450308937c074c543
