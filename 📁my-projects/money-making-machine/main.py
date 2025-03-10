import streamlit as st
import random
import time
import requests

st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money...")
    time.sleep(5)
    amount = generate_money()
    st.warning(f"You made ${amount}!")

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
            return("Freelancing - Start offering your skills online!")
        
    except:
        return ("Something went wrong!")
    
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle:"):
    idea = fetch_side_hustle()
    st.success(idea)
        
def fetch_money_quotes():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return  quotes["money_quotes"]
        else:
            return("Money is the root of all evil")
        
    except:
        return ("Something went wrong!")
    
st.subheader("Money Making Motivation")
if st.button("Get Inspired:"):
    quote = fetch_money_quotes()
    st.info(quote)
