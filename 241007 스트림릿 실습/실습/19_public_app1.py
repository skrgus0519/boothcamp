import streamlit as st
import pandas as pd
import plotly.express  as px

from time import time

# [TODO] 아래 summary를 참고하여 막대 그래프와 라인 그래프를 그리는 함수를 구성해봅니다.
"""_summary_
fig = px.bar(bar_df, 
                title="",
                y='',
                color="",
                hover_data='')

fig = px.line(line_df,x="일시",y="",
            title="",
            color='',
            line_group='',
            hover_name="")
"""

## *geo는 클릭이 된 지역구들이 들어있는 튜플이라고 생각하시면 됩니다. 

def bar_chart(*geo):
    
    return fig
    
def line_chart(*geo):
    
    return fig


# 페이지 구성
df = pd.read_csv("seoul.csv")
st.title("서울시 미세먼지 분포")


## 각 지역별 미세먼지, 초미세먼지 평균을 알아보기 위해 pivot_table을 활용해봅시다. 


##  column으로 구역을 나눠줍니다 

# 왼쪽 column의 내용을 채워줍니다. 

# 체크 표시된 지역구만 뽑아서 리스트로 저장합니다.

# 오른쪽 column의 내용을 채워줍니다. (Tab 두개를 만들어줍니다. )
