import streamlit as st
import pandas as pd
import random
# import gspread_pandas as gpd
# from gspread_pandas import Spread
# s=Spread('me','Questions2019B')
import xlrd

@st.cache(allow_output_mutation=True)
def get_data(url):
    return pd.read_csv(Url,encoding='utf-8')

@st.cache
def get_subj(labs):
    subj= labs.sample(n=3)
    lst = subj.values.tolist()
    return  lst

@st.cache(allow_output_mutation=True)
def get_dict():
    return {}

@st.cache(allow_output_mutation=True)
def get_history():
    return []

@st.cache(allow_output_mutation=True)
def get_labs(shelot):
    return shelot['מעבדה'].drop_duplicates().sample(frac=1)

@st.cache(allow_output_mutation=True)
def get_question(shelot,koshi,sbject):
    return shelot[(shelot['רמת_קושי'] == koshi) & (shelot['מעבדה'] == sbject) & (shelot['was_asked'] == 0)].sample(n=1)


radioDict={
    1:'שאלות על המעבדות השונות',
    2:'שאלות על הפרוייקט'
}


Url='https://docs.google.com/spreadsheets/d/16l-wvB6zJz9GdxussYA3dYL4Ovb7-M1xYayXzoR_j_k/export?format=csv'
shelot=get_data(Url)
###
# temp=shelot[['מעבדה','רמת_קושי']]
# tmp=temp.groupby( ['מעבדה' , 'רמת_קושי' ]).size()
# st.table(tmp)
###
options=shelot['project'].drop_duplicates().tolist()
project = st.sidebar.selectbox('Choose project from  list', options)
students=shelot[(shelot['project']==project)]['students']
labs=get_labs(shelot)
mode=st.sidebar.radio( 'בחר צורת הפעלה' ,(1,2),format_func=radioDict.get)
student=st.sidebar.selectbox('בחר סטודנט' ,students.tolist())
history=get_dict()
if mode==1:
    koshi=st.sidebar.radio('קושי', (1,2,3))
    sbject=st.sidebar.selectbox( 'בחר נושא' ,labs.values)
    tmp=get_question(shelot,koshi,sbject)
    if st.sidebar.button('שאלה'):
        if not history.get(student ):
            history[student ]=[]
        indx = tmp.index + 2
        history[student ].append(indx.astype('str', copy = False))
        st.table(tmp[['שאלה']])
    if st.sidebar.button('תשובה'):
        st.table(tmp[['תשובה']])
else:
    if st.sidebar.button('question'):
        q=shelot[(shelot['students']==student)]['question']
        st.table(q)
        if not history.get(student ):
            history[student ]=[]
        history[student].append('Project_question')
number = st.sidebar.selectbox('Grade student b4 pressing the button', options=[i for i in range(-1, 4)])
if st.sidebar.button('Grade?'):
    if number > -1:
        history[student].append(number)
if st.sidebar.button('History?'):
    st.write('אלו האינדקסים של מספרי השאלות שנשאלו עכשיו אנא עדכנו את הקובץ')
    st.table([[(k,vv) for vv in v] for k,v in history.items()])





