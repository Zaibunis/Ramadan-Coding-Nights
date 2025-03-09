import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Configure the Streamlit app's appearance and layout
# 'page_title' sets the browser tab title
# 'layout="wide"' allows more horizontal space, improving the display for tables and graphs
st.set_page_config(page_title="Data Sweeper", layout="wide")

# Custom CSS for styling the app with dark mode aesthetics
# This enhances the UI by setting background colors, button styles, and text formatting


# Custom CSS Styling for Layout
st.markdown(
    """
    <style>
        /* Overall Page Layout */
        .main {
            background-color: #0d1117;
        }
        .block-container {
            padding: 2.5rem 2rem;
            border-radius: 12px;
            background-color: #161b22;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
        
        
        
/* Left Section - Unit Information & Conversion Summary */
        .left-panel {
            background-color: #161b22;
            padding: 1.5rem;
            border-radius: 12px;
            width: 30%;
            position: fixed;
            left: 1rem;
            top: 1rem;
            height: 90%;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }
        
        .section-title {
            font-size: 1.5rem;
            font-weight: bold;
            color: #58a6ff;
            margin-bottom: 1rem;
        }
        
        .info-box, .summary-box {
            background-color: #0d1117;
            padding: 1rem;
            border-radius: 8px;
            color: white;
            font-size: 0.9rem;
            margin-bottom: 1rem;
        }
        

        /* Buttons Styling */
      
          .clear-history-button>button {
            background-color: #c33c3c !important;
            display: block;
            margin: 50px auto !important;
            text-align: center;
        }
        .clear-history-button>button:hover {
            background-color: #a02d2d !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


   

# Dictionary containing unit information for different categories
unit_info = {
    "Length": "📏 Length measures the distance between two points. Common units: meters, kilometers, miles.",
    "Weight": "⚖️ Weight measures the mass of an object. Common units: kilograms, grams, pounds.",
    "Temperature": "🌡 Temperature indicates the degree of heat. Common units: Celsius, Fahrenheit, Kelvin.",
    "Speed": "🚀 Speed measures how fast an object moves. Common units: km/h, m/s, mph.",
    "Time": "⏳ Time measures duration. Common units: seconds, minutes, hours.",
    "Area": "📐 Area measures the size of a surface. Common units: square meters, acres, hectares.",
    "Volume": "🧪 Volume measures the amount of space an object occupies. Common units: liters, cubic meters, gallons.",
    "Energy": "⚡ Energy represents the ability to do work. Common units: joules, calories, kilowatt-hours."
}

# Dictionary for unit conversion factors
conversion_factors = {
    "Length": {
        "Meters to Kilometers": lambda x: x / 1000,
        "Kilometers to Meters": lambda x: x * 1000
    },
    "Weight": {
        "Kilograms to Pounds": lambda x: x * 2.20462,
        "Pounds to Kilograms": lambda x: x / 2.20462
    },
    "Temperature": {
        "Celsius to Fahrenheit": lambda x: (x * 9/5) + 32,
        "Fahrenheit to Celsius": lambda x: (x - 32) * 5/9
    },
    "Speed": {
        "Kilometers per hour to Miles per hour": lambda x: x * 0.621371,
        "Miles per hour to Kilometers per hour": lambda x: x / 0.621371
    },
    "Time": {
        "Seconds to Minutes": lambda x: x / 60,
        "Minutes to Hours": lambda x: x / 60,
        "Hours to Seconds": lambda x: x * 3600
    },
    "Area": {
        "Square Meters to Acres": lambda x: x / 4046.86,
        "Acres to Square Meters": lambda x: x * 4046.86
    },
    "Volume": {
        "Liters to Gallons": lambda x: x * 0.264172,
        "Gallons to Liters": lambda x: x / 0.264172
    },
    "Energy": {
        "Joules to Calories": lambda x: x / 4.184,
        "Calories to Joules": lambda x: x * 4.184
    }
}

st.title("🔄 Unit Converter")

# Sidebar Section: Unit Information & Conversion History
with st.sidebar:
    st.markdown("<p class='section-title'>📌 Unit Information</p>", unsafe_allow_html=True)
    
    # Display the relevant unit info
    st.markdown(
        f"<div class='info-box'>{unit_info.get(st.session_state.get('category', 'Length'))}</div>",
        unsafe_allow_html=True
    )
    
    st.markdown("<p class='section-title'>📜 Conversion History</p>", unsafe_allow_html=True)
    
    # Retrieve last conversion from session state
    summary = st.session_state.get("last_conversion", "No recent conversion")
    st.markdown(f"<div class='summary-box'>{summary}</div>", unsafe_allow_html=True)

    # Clear history button
    if st.button("🗑️ Clear History", key="clear"):
        st.session_state["last_conversion"] = "No recent conversion"
        st.rerun()

# Main Section: Unit Converter
unit_category = st.selectbox("Select a Category", list(conversion_factors.keys()), key="category")

# Dynamically update conversion options
conversion_type = st.selectbox("Select Conversion", list(conversion_factors[unit_category].keys()), key="conversion")
input_value = st.number_input("Enter value:", min_value=0.0, format="%.2f", key="value")

# Convert Button
if st.button("Convert", key="convert"):
    result = conversion_factors[unit_category][conversion_type](input_value)
    st.success(f"Converted Value: {result:.2f}")
    
    # Store last conversion
    summary_text = f"{input_value} → {result:.2f} ({conversion_type})"
    st.session_state["last_conversion"] = summary_text

# Reset Button
if st.button("Reset", key="reset"):
    st.rerun()