import streamlit as st
import random

st.title("Quiz Application")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Quetta"],
        "answer": "Islamabad"
    },
    {
       "question": "What is the capital of Pakistan?",
        "options": ["Karachi", "Lahore", "Islamabad", "Quetta"],
        "answer": "Islamabad"
    },
    {
    "question": "Who is the founder of Pakistan?",
    "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Sir Syed Ahmed Khan"],
    "answer": "Muhammad Ali Jinnah"
}
,
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Dollar", "Rupee", "Euro", "Yen"],
        "answer": "Rupee"
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Karachi", "Multan"],
        "answer": "Karachi"
    },
    {
        "question": "What is the national animal of Pakistan?",
        "options": ["Lion", "Markhor", "Tiger", "Eagle"],
        "answer": "Markhor"
    } 
]

# Ensure session state variable exists
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("Correct!")
        st.balloons()
    else:
        st.error("Incorrect! The correct answer is " + question["answer"])
        st.snow()
       

# Update the question only after submitting an answer
if "answered" not in st.session_state:
    st.session_state.answered = False

if st.session_state.answered:
    st.session_state.current_question = random.choice(questions)
    st.session_state.answered = False
    st.rerun()

if st.button("Next Question"):
    st.session_state.current_question = random.choice(questions)
    st.session_state.answered = True
    st.rerun()
