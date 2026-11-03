
import streamlit as st
import random

st.title("🎮 Number Guessing Game")
st.write("I have selected a number between 1 and 100.")
st.write("You have only 7 attempts!")

# Initialize game
if "num" not in st.session_state:
    st.session_state.num = random.randint(1, 100)
    st.session_state.tries = 0
    st.session_state.game_over = False
    st.session_state.won = False

# User input
if not st.session_state.game_over:

    guessing = st.number_input(
        "Enter your guessing number:",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("Guess"):

        st.session_state.tries += 1

        if guessing < st.session_state.num:
            st.warning("Too Low! Try Again.")

        elif guessing > st.session_state.num:
            st.warning("Too High! Try Again.")

        else:
            st.success("YOU WIN!")
            st.write(
                f"You guessed it in {st.session_state.tries} attempts."
            )
            st.session_state.won = True
            st.session_state.game_over = True

        if st.session_state.tries >= 7 and not st.session_state.won:
            st.session_state.game_over = True
            st.error("Game Over!")
            st.write("Correct number was:", st.session_state.num)

# Restart game
if st.session_state.game_over:

    if st.button("Play Again"):
        st.session_state.num = random.randint(1, 100)
        st.session_state.tries = 0
        st.session_state.game_over = False
        st.session_state.won = False
        st.rerun()
