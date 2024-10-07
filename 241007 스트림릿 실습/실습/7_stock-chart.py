import streamlit as st
import FinanceDataReader as fdr
import datetime

# Finance Data Reader
# https://github.com/financedata-org/FinanceDataReader

date = st.date_input('조희 시작일을 선택해주세요',
              datetime.datetime(2022,1,1))

code = st.text_input('종목코드', value='', placeholder='종목코드를 입력해주세요')


if date and code:
    df = fdr.DataReader(code, date)
    data = df.sort_index(ascending=True).loc[:, 'close'] # OHLCV
    st.line_chart(data)