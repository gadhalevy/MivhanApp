import streamlit as st
import pandas as pd
import gspread_pandas as gpd
# from gspread_pandas import Spread
# s=Spread('me','Questions2019B')
import xlrd


@st.cache
def get_subj(labs):
    subj= labs.sample(n=3)
    lst = subj.values.tolist()
    return  lst

@st.cache(allow_output_mutation=True)
def get_state():
    return []

@st.cache(allow_output_mutation=True)
def get_history():
    return []

radioDict={
    1:'ידנית',
    2:'אוטומטית'
}


Url='https://docs.google.com/spreadsheets/d/16l-wvB6zJz9GdxussYA3dYL4Ovb7-M1xYayXzoR_j_k/export?format=csv'
shelot=pd.read_csv(Url,encoding='utf-8',skiprows=14)
projects=pd.read_excel('marks2020B.xlsx')
options=projects['שם_פרויקט'].drop_duplicates().tolist()
project = st.sidebar.selectbox('Choose project from  list', options)
# st.table(projects)
students=projects[(projects['שם_פרויקט']==project)]['סטודנטים']
labs=shelot[['מעבדה']].drop_duplicates()
mode=st.sidebar.radio( 'בחר צורת הפעלה' ,(1,2),format_func=radioDict.get)
history=get_history()
if mode==1:
    student=st.sidebar.selectbox('בחר סטודנט' ,students.tolist())
    koshi=st.sidebar.radio('קושי', (1,2,3))
    sbject=st.sidebar.selectbox( 'בחר נושא' ,labs.values.tolist())
    if st.sidebar.button('שאל'):
        tmp=shelot[(shelot['רמת_קושי']==koshi) & (shelot['מעבדה']==sbject[0]) & (shelot['was_asked']==0)].sample(n=1)
        history.append(tmp.index+16)
        st.table(tmp[['שאלה']])
        st.table(tmp[['תשובה']])
else:
    state = get_state()
    state.append(len(state))
    labIndx=state[-1]%len(labs)
    koshiIndx=state[-1]%3+1
    st.write('רמת קושי' ,koshiIndx)
    lab=labs.values.tolist()[labIndx][0]
    st.write(lab)
    tmp = shelot[(shelot['רמת_קושי'] == koshiIndx) & (shelot['מעבדה'] == lab) & (shelot['was_asked'] == 0)].sample(n=1)
    history.append(tmp.index+16)
    st.table(tmp[['שאלה']])
    st.table(tmp[['תשובה']])
    st.sidebar.button('Ask')
if st.sidebar.button('History?'):
    st.write('אלו האינדקסים של מספרי השאלות שנשאלו עכשיו אנא עדכנו את הקובץ')
    st.table(history)




    # if st.sidebar.button('בחר שאלה'):
    #     tmp=df[(df['רמת_קושי']==2) & (df['מעבדה']==nose[0][0])].sample(n=1)
    #     # print(df[(df['רמת_קושי']==2)])
    #     st.info(tmp)
    #
    #     st.table(tmp[['שאלה']])
    #     st.table(tmp[['תשובה']])
    # quest=df[(['רמת_קושי']==koshi) & ]
    # labs=[l for l in labs if not l.isnumeric()]



# if st.sidebar.button('בחר שאלה'):
#     st.write(df[(df['רמת קושי']==2) & (df['מעבדה']=='IOT')].sample(n=1)['שאלה'])
# print (df[(df['רמת קושי']==2) & (df['מעבדה']=='IOT')].sample(n=1)['שאלה'])



