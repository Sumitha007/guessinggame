import streamlit as st
import random

# Set a title
st.title("Number Guessing Game")

# Define the range for the number
min_num = 1
max_num = 100

# Initialize the game state
if "target" not in st.session_state:
    st.session_state.target = random.randint(min_num, max_num)
    st.session_state.attempts = 0

# Display instructions
st.write(f"Guess the number between {min_num} and {max_num}!")

# Input box for the user's guess
guess = st.number_input("Enter your guess:", min_value=min_num, max_value=max_num, step=1)

# Button to submit the guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1

    # Check if the guess is correct, too low, or too high
    if guess == st.session_state.target:
        st.success(f"🎉 Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
        st.write("Click 'Restart Game' to play again!")
    elif guess < st.session_state.target:
        st.warning("Try a higher number.")
    else:
        st.warning("Try a lower number.")

# Button to restart the game
if st.button("Restart Game"):
    st.session_state.target = random.randint(min_num, max_num)
    st.session_state.attempts = 0
    st.info("Game restarted! Try guessing the new number.")

