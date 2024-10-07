import streamlit as st

# 타이틀 적용 예시
st.title('제목입니다.')
# 특수 이모티콘 삽입 예시
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.title('100점!:100:')

# Header 적용
st.header('header')

# Subheader 적용
st.subheader('subheader')

# 캡션 적용
st.caption('caption')

# 코드 표시
sample_code = '''
def func():
    print('function!')
'''
st.code(sample_code, language='python')

# 일반 텍스트
st.text('text.')

# 마크다운 문법 지원
st.markdown('**Hello**!')

# 컬러코드: blue, green, orange, red, violet
st.markdown(':blue[파랑], :red[빨강], :orange[주황], :green[초록], **:violet[바이올렛]**')

# latex 수식
st.markdown('$\sqrt{x^2+y^2}=1$')

# LaTex 수식 지원
st.latex(r'\sqrt{x^2+y^2}=1')