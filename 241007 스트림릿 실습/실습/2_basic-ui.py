import streamlit as st
import pandas as pd
from datetime import datetime as dt
import datetime

# 버튼 클릭
button = st.button('버튼을 눌러보세요')

if button:
    st.write('버튼이 눌렸습니다.')
else:
    st.write('버튼을 눌러주세요.')

# 파일 다운로드 버튼
# 샘플 데이터 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})


# 다운로드 버튼 연결
st.download_button(
    label='다운로드 버튼',
    data = dataframe.to_csv(),
    file_name='sample.csv',
    mime= 'text/csv'  # 그림이면 image/png
)


# 체크 박스
agree = st.checkbox('동의하시겠습니까?')

if agree:
    st.write('동의해주셔서 감사합니다.')

# 라디오 선택 버튼
blood = st.radio('당신의 혈액형은 무엇입니까?',('A','B','O','AB'))

if blood == 'A':
    st.write('A형이시네요!')
elif blood == 'B':
    st.write('B형이시네요!')
elif blood == 'O':
    st.write('O형이시네요!')
elif blood == 'AB':
    st.write('AB형이시네요!')

# 선택 박스
st.selectbox('당신의 혈액형은 무엇입니까?',('A','B','O','AB'), index=2)

# 다중 선택 박스
fruits = st.multiselect('당신이 좋아사는 과일이 뭔가요?',
                ['사과', '바나나', '오렌지', '포도'],
                ['사과', '오렌지'])

# st.write('당신은 {}를 좋아하시네요!'.format(fruits))

st.write(f'당신은 {fruits}를 좋아하시네요!')

# 슬라이더
st.slider('약속시간은 언제로 할까요?',
            min_value=dt(2020,1,1,0,0),
            max_value=dt(2021,1,1,0,0),
            step=datetime.timedelta(hours=1),
            format='MM/DD/YY ~ HH:mm')

# 텍스트 입력
st.text_input(label='가장 좋아하는 동물은?', placeholder='동물을 입력해주세요.')


# 숫자 입력
st.number_input(label = '시험점수를 입력해주세요',
                min_value = 0,
                max_value = 100)
