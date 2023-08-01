import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

#글씨 크기
st.title("this is title, 제일 큼")
st.header("this is header, 그 다음 큼")
st.subheader("this is subheader, 그 다음 큼")

#페이지 공간 레이아웃
col1, col2 = st.columns([1,1])

with col1:
    st.title("it is column1 here")
    st.checkbox("this is checkbox1 in col1")

with col2:
    st.title("this is column2")
    st.checkbox('this is checkbox2')

col1.subheader('this is subheader of col1')
col2.checkbox('second checkbox in col2')

#탭 생성
tab1, tab2 = st.tabs(['tab A', 'tab B'])

with tab1:
    st.write("this is tab A content")
    st.button("click here")

with tab2:
    st.write("this is content in tab B")
    st.button("okay")

#사이드바 생성
st.sidebar.title('this is sidebar')
option = st.sidebar.selectbox('what do you think?',
                              ('read', 'listen', 'speak','write'))

st.sidebar.write('you selected: ', option)

#이미지 불러오기
zzang = Image.open('zzangnan.jpg')
st.sidebar.image(zzang, width=300)

#sklearn에서 아이리스 데이터 가져오기
iris = load_iris()

st.title('iris_data_set')
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df.columns = [col_name.split(' (cm)')[0] for col_name in df.columns]
df['species'] = iris.target

species_dict={0:'setosa', 1:'versicolor', 2:'virginica'}

def mapp_species(x):
    return species_dict[x]

df['species'] = df['species'].apply(mapp_species)
df

st.subheader('this is table')
st.table(df.head())

st.subheader('this is dataframe')
st.dataframe(df.head())

st.sidebar.title('iris species🌸')
#select(단일)
# select_species = st.sidebar.selectbox(
#     '확인하고 싶은 종을 선택하세요(10행 미리보기)',
#     ['setosa', 'versicolor', 'virginica']
# )

# temp_df = df[df['species'] == select_species]

# st.table(temp_df.head(10))

#multi select(복수)
selectmulti = st.sidebar.multiselect(
    '확인하고 싶은 종을 선택하세요. 중복 가능',
    ('setosa', 'versicolor', 'virginica')
    )

temp_df = df[df['species'].isin(selectmulti)]
st.table(temp_df)

#라디오 변수..?
radio_select =st.sidebar.radio(
    "what is key column?",
    ['sepal length', 'sepal width', 'petal length','petal width'],
    horizontal=True
    )
#컬럼의 값 범위 조정하는 slider
slider_range = st.sidebar.slider(
    "choose range of key column",
    0.0,  #시작 값
    10.0,  #끝 값
    (2.5, 7.5)  #기본값
)
#필터 적용버튼 생성, 버튼이 눌리면 true 값으로 바뀜
#이를 이용해서 if문 사용, 눌렸을 때 구현
start_button = st.sidebar.button(
    'filter apply 🚥'
)

if start_button:
    tmp_df = df[df['species'].isin(selectmulti)]
    tmp_df = tmp_df[(tmp_df[radio_select] >= slider_range[0])&
                    (temp_df[radio_select] <= slider_range[1])]
    st.table(tmp_df)
    st.sidebar.success('applied!')

#slider_range[0]: 최솟값
#slider_ragne[1]: 최댓값

st.title('exx')