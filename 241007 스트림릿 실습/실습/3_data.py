import streamlit as st
import pandas as pd
import numpy as np


st.title('데이터프레임 튜토리얼')

# DataFrame 생성
dataframe = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
})

# DataFrame
st.dataframe(dataframe, use_container_width=False)
st.dataframe(dataframe, use_container_width=True)

# data_editor 
# 표에서 데이터 수정 가능

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

edited_df = st.data_editor(df)
favorite_command = edited_df.loc[edited_df['rating'].idxmax()]['command']
st.markdown('Favorite command is {}'.format(favorite_command))



# 테이블(static)
# DataFrame과는 다르게 interactive 한 UI 를 제공하지 않습니다.
st.table(dataframe)

# # 메트릭
st.metric(label="온도", value="10°C", delta="-1.2°C")
st.metric(label="삼성전자", value="58000원", delta="-2800원")

# 컬럼으로 영역을 나누어 표기한 경우
col1,col2,col3 = st.columns(3)

col1.metric(label="삼성전자", value="58000원", delta="-2800원")
col2.metric(label="SK하이닉스", value="170000원", delta="1800원")

with col3:
    st.metric(label="현대차", value="240000원", delta="3500원")