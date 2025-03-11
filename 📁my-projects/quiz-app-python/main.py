import streamlit as st
import random
import time

# 🎨 Fun Title with Emoji
st.title("🧠🎯 Ultimate Quiz Challenge!")

# 🎵 Sound or GIF (if you want to add media)
st.markdown("Get ready to test your knowledge! 🚀💡")

questions = [
    {
        "question": "🏙️ What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Quetta"],
        "answer": "Islamabad"
    },
    {
       "question": "🗺️ Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Karachi", "Multan"],
        "answer": "Karachi"
    },
    {
        "question": "👑 Who is the founder of Pakistan?",
        "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Sir Syed Ahmed Khan"],
        "answer": "Muhammad Ali Jinnah"
    },
    {
        "question": "💰 What is the currency of Pakistan?",
        "options": ["Dollar", "Rupee", "Euro", "Yen"],
        "answer": "Rupee"
    },
    {
        "question": "🦌 What is the national animal of Pakistan?",
        "options": ["Lion", "Markhor", "Tiger", "Eagle"],
        "answer": "Markhor"
    }
]


if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)
    st.session_state.answered = False

question = st.session_state.current_question

st.subheader(f"Question: {question['question']}")

selected_option = st.radio("🤔 Choose your answer:", question["options"], key="answer")

if st.button("🚀 Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Woohoo! Correct Answer! 🎉🥳")
        st.balloons()  # 🎈 Celebration effect
    else:
        st.error(f"❌ Oops! Incorrect! The correct answer is **{question['answer']}** 💡")
        st.snow()  # ❄️ Fun effect for incorrect answers

  
if st.button("🎲 New Random Question"):
    st.session_state.current_question = random.choice(questions)
    st.session_state.answered = True
    st.rerun()


