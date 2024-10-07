import streamlit as st
import FinanceDataReader as fdr
import datetime
import time

# Finance Data Reader
# https://github.com/financedata-org/FinanceDataReader

st.title('종목 차트 검색')


### 좌측 사이드바 - 조회 시작일, 종목 코드 작성란 만들기
with st.sidebar:
    date = st.date_input('조희 시작일을 선택해주세요',
              datetime.datetime(2022,1,1))

    code = st.text_input('종목코드', value='', placeholder='종목코드를 입력해주세요')


### 날짜, 종목코드 입력되면 차트 생성 - 탭 2개로 생성(탭1 : 차트, 탭2: 데이터(Dataframe))
if date and code:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'close'] # OHLCV
    
    tab1, tab2 = st.tabs(['차트', '데이터'])

    with tab1:
        st.line_chart(data)

    with tab2:
        st.dataframe(df.sort_index(ascending=True))

    with st.expander('컬럼 설명'):
        st.markdown('''
                    - Open: 시가
                    - High: 고가
                    - Low: 저가
                    - Close: 종가
                    - Adj Close: 수정 종가
                    - Volune: 거래량
                    ''')