import streamlit as st
import openai

openai.api_key = "API_KEY"

# 채팅 히스토리 초기화 ('messages' 라는 빈 리스트를 session state에 저장해줍니다.)

# 
with st.chat_message("assistant"):
    st.write("안녕하세요! 무엇이든 제가 영어로 번역해드릴게요!")

prompt = st.chat_input("번역할 문장")


if prompt:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}\n위 문장을 영어로 변역해줄 수 있니?"}]
    )
    st.session_state.messages.append((prompt,completion["choices"][0]["message"]["content"]))

for prompt, answer in st.session_state.messages:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(answer) 