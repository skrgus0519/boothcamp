# 깃허브 ReadMe 디자인 해보기
# 제출 형식 맞게 best.pt가지고 예측 코드 짜기
# (gpt한테 best.pt가지고 폴더안에 이미지 여러장 예측하려고 하는데 출력 형식을 ~~~형식으로 하고 싶어)
# 출력 형식 : 이미지(바운딩박스 그려진), txt파일(id, 박스좌표 포함), 클래스 ID는 0, 1 적혀있는거
# -> 0~5로 형태를 만들어두고 나중에 변경, 박스 좌표가 아닌 X, Y 좌표
# Streamlit에 이미지 넣으면 예측 이미지 나오도록 구현

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title(":man-walking:보행자 무단횡단 탐지 프로그램:vertical_traffic_light:")

# 파일 업로드
uploaded_file = st.file_uploader("이미지 파일을 업로드하세요", type=["jpg", "png", "jpeg"])

# 업로드된 파일이 있을 경우
if uploaded_file is not None:
    # 업로드된 이미지를 PIL로 읽기
    image = Image.open(uploaded_file)
    
    # 이미지 표시
    st.image(image, caption='업로드한 이미지', use_column_width=True)