import streamlit as st
import random

if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

st.title("Number Guessing Game")
guess = st.number_input("Guess a number between 1 and 100", min_value=1, max_value=100, step=1)

if st.button("Submit"):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.write("Too low!")
    elif guess > st.session_state.number:
        st.write("Too high!")
    else:
        st.write(f"Correct! It took you {st.session_state.attempts} attempts.")
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0