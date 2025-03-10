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
        # Try to get data from local server
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:  # If request successful
            hustles = response.json()  # Convert response to JSON
            return hustles["side_hustles"]  # Return the hustle idea
        else:
            return "Freelancing"  # Default response if server fails

    except Exception as e:  # Added error logging
        print(f"Error: {e}")  # This will help debug the issue
        return "Something went wrong!"  # Error message if request fails


# Create a section for side hustle ideas
st.subheader("Side Hustle Ideas")
if st.button("Generate Hustle"):  # When user clicks button
    idea = fetch_side_hustle()  # Get a hustle idea
    st.success(idea)  # Show the idea


# Function to get money-related quotes from server
def fetch_money_quote():
    try:
        # Try to get quote from local server
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:  # If request successful
            quotes = response.json()  # Convert response to JSON
            return quotes["money_quotes"]  # Return the quote
        else:
            return "Money is the root of all evil!"  # Default quote if server fails
    except Exception as e:  # Added error logging
        print(f"Error: {e}")  # This will help debug the issue
        return "Something went wrong!"  # Error message if request fails


# Create a section for motivation quotes
st.subheader("Money-Making Motivation")
if st.button("Get Inspired"):  # When user clicks button
    quote = fetch_money_quote()  # Get a quote
    st.info(quote)  # Show the quote