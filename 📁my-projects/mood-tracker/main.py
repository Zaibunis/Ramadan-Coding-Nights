import streamlit as st
import pandas as pd
import datetime
import csv
import os

MOOD_FILE = "mood_log.csv"

# Function to load mood data
def load_mood_data():
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        df = pd.DataFrame(columns=["Date", "Mood"])
        df.to_csv(MOOD_FILE, index=False)  # Ensure headers are written
        return df

    try:
        df = pd.read_csv(MOOD_FILE)
        if "Date" not in df.columns or "Mood" not in df.columns:
            return pd.DataFrame(columns=["Date", "Mood"])
        return df
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=["Date", "Mood"])

# Function to save mood data
def save_mood_data(date, mood):
    if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
        with open(MOOD_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Mood"])
    
    with open(MOOD_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# Streamlit UI
st.title("Mood Tracker 😊")

today = datetime.date.today()

st.subheader("How are you feeling today?")

mood = st.selectbox("Select your mood", ["Happy", "Sad", "Angry", "Stressed", "Anxious", "Neutral", "Excited"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood logged successfully! 🎉")

# Load data and show trends
data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends Over Time 📊")

    try:
        # Ensure 'Date' column exists before conversion
        if "Date" in data.columns:
            data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
            data.dropna(subset=["Date"], inplace=True)
        
        # Count occurrences of each mood
        mood_counts = data["Mood"].value_counts()

        # Debugging output
        st.write("Mood Counts Data:", mood_counts)

        # Display bar chart
        if not mood_counts.empty:
            st.bar_chart(mood_counts)
        else:
            st.write("No mood data available yet. Log your mood to see the graph!")

    except Exception as e:
        st.error(f"Error processing data: {e}")

    # Show mood data tabl
    st.write("### Logged Mood Data 📝")
    st.dataframe(data.sort_values(by="Date", ascending=False))

st.write("Build with ❤️ by [Faria Mustaqim](https://github.com/Zaibunis)")