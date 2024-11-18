import streamlit as st


if 'low' not in st.session_state:
    st.session_state.low, st.session_state.high = 1, 100


guess = (st.session_state.low + st.session_state.high) // 2
st.write(f"Is your number {guess}?")


feedback = st.radio("Feedback:", ["Too low", "Too high", "Correct"])

if feedback == "Too low":
    st.session_state.low = guess + 1
elif feedback == "Too high":
    st.session_state.high = guess - 1
elif feedback == "Correct":
    st.write(f"Yay! The computer guessed {guess} correctly!")
    st.session_state.low, st.session_state.high = 1, 100  
