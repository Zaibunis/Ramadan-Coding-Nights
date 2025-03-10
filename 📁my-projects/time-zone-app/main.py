import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "America/Los_Angeles",
    "Europe/London",
    "Asia/Shanghai",
    "Australia/Sydney",
]

st.title("Time Zone App")

selected_timezone = st.multiselect("Select Timezones", TIME_ZONES, default=["UTC","Asia/Karachi"])

st.subheader("Selected Timezones")

for tz in selected_timezone:
                                                    
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")#y stands for year, m stands for month, d stands for day, I & p stands for 12 hour format, H stands for hour, M stands for minute, S stands for second, %p stands for AM/PM
  
    st.write(f"**{tz}**: {current_time}")

st.subheader("Timezone Converter")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_timezone = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_timezone = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):

    dt=datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_timezone))

    converted_time = dt.astimezone(ZoneInfo(to_timezone)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.success(f"Converted Time in {to_timezone} is: {converted_time}")