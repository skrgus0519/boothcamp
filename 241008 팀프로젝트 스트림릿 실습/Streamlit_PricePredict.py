import streamlit as st
import pandas as pd

# df = pd.read_csv('맨하탄주택가격.csv')

st.title(':house:맨하탄주택가격예측:heavy_dollar_sign:')

with st.expander('변수에 대한 설명'):
    list = ['bedrooms: 침실의 개수', 'bathrooms: 욕실의 개수', 'size_sqft: 주택의 면적(제곱피트 단위)', 'min_to_subway: 지하철역까지의 거리(분 단위)', 'floor: 주택의 층수',
        'building_age_yrs: 건물의 연식', 'no_fee: 중개 수수료 여부 (1 = 중개 수수료 없음, 0 = 있음)', 'has_roofdeck: 루프덱(옥상 테라스)이 있는지 여부 (1 = 있음, 0 = 없음)',
        'has_washer_dryer: 세탁기와 건조기가 있는지 여부 (1 = 있음, 0 = 없음)', 'has_doorman: 도어맨이 있는지 여부 (1 = 있음, 0 = 없음)', 'has_elevator: 엘리베이터가 있는지 여부 (1 = 있음, 0 = 없음)',
        'has_dishwasher: 식기세척기가 있는지 여부 (1 = 있음, 0 = 없음)', 'has_gym: 헬스장이 있는지 여부 (1 = 있음, 0 = 없음)']
    for i in list:
        st.caption(i)

st.number_input(label='침실의 개수를 입력하세요.',
                min_value=0,
                max_value=5)

st.number_input(label='욕실의 개수를 입력하세요.',
                min_value=0,
                max_value=5)

st.slider('주택의 면적을 정해주세요. (단위: ft²)', 250, 4800, step=1)

st.slider('지하철역까지 걸리는 시간(단위: 분)', 0, 43, step=1)

st.slider('주택의 층 수를 정해주세요.', 0.0, 83.0, step=0.5)

st.slider('건물의 연식을 정해주세요.', 0, 180, step=1)

st.selectbox('중계 수수료를 지불할 의향이 있으신가요?', ('Yes','No'), index=1)

st.selectbox('옥상에 테라스가 있는 건물을 원하시나요?', ('Yes','No'), index=0)

st.selectbox('내부에 세탁기와 건조기가 있는 건물을 원하시나요?', ('Yes','No'), index=0)

st.selectbox('도어맨이 근무하는 건물을 원하시나요?', ('Yes','No'), index=1)

st.selectbox('엘레베이터가 작동하는 건물을 원하시나요?', ('Yes','No'), index=0)

st.selectbox('식기세척기가 있는 건물을 원하시나요?', ('Yes','No'), index=1)

st.selectbox('내부에 헬스장이 있는 건물을 원하시나요?', ('Yes','No'), index=0)

st.multiselect('건물에 원하는 옵션을 선택해주세요.', ['루프덱(옥상 테라스)', '세탁기와 건조기', '도어맨', '엘리베이터', '식기세척기', '헬스장'])


# 'bedrooms': number_input, 'bathrooms': number_input, 'size_sqft': number_input or slider, 'min_to_subway': number_input, 'floor': number_input or slider
# 'building_age_yrs': number_input or slider, 'no_fee': selectbox, 'has_roofdeck': selectbox, 'has_washer_dryer': selectbox, 'has_doorman':selectbox
# 'has_elevator': selectbox, 'has_dishwasher': selectbox, 'has_gym': selectbox