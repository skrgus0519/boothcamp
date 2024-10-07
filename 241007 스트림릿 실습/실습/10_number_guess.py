import streamlit as st
import random


st.title(':game_die:숫자 추측 게임:game_die:')
if 'random_number' not in st.session_state:
    st.session_state.random_number = random.randint(1,100)

user_guess = st.number_input('1에서 100사이의 숫자를 입력하세요:', min_value=1, max_value=100, step=1)

guess_button = st.button('추측하기')

if guess_button:
    if user_guess < st.session_state.random_number:
        st.write('너무 낮습니다! 다시 시도하세요.')
    elif user_guess > st.session_state.random_number:
        st.write('너무 높습니다! 다시 시도하세요.')
    else:
        st.success('축하합니다! 정답은 {}입니다.'.format(user_guess))

if st.button('게임 재시작'):
    st.session_state.random_number = random.randint(1,100)
    st.write('게임이 재시작되었습니다!')