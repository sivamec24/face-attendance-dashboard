import streamlit as st
import pandas as pd
import time
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import os

# ✅ Set page config
st.set_page_config(
    page_title="Face Attendance Dashboard",
    layout="wide",
)

# ✅ Inject custom CSS for background and styling
st.markdown("""
    <style>
    /* Set background image */
    body {
        background-image: url('https://images.unsplash.com/photo-1521791136064-7986c2920216?fit=crop&w=1400&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }

    /* Transparent container */
    .stApp {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 10px;
    }

    /* Customize text */
    h1, h2, h3, h4 {
        color: #2E3B55;
    }

    /* Dataframe styling */
    .css-1r6slb0 {
        background-color: white;
        border-radius: 8px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        padding: 1rem;
    }

    </style>
""", unsafe_allow_html=True)

# ✅ Get current date and time
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# ✅ Title and last update time
st.title("📋 Face Recognition Attendance Dashboard")
st.markdown(f"🕒 **Last updated:** `{timestamp}`")

# ✅ Auto-refresh every 2 seconds
st_autorefresh(interval=2000, limit=None, key="autorefresh")

# ✅ Path to today's attendance file
attendance_file = f"Attendance/Attendance_{date}.csv"

# ✅ Load and display attendance data
if os.path.exists(attendance_file):
    df = pd.read_csv(attendance_file)
    st.subheader("✅ Attendance Records")
    st.dataframe(df.style.highlight_max(axis=0), use_container_width=True)
else:
    st.warning("⚠️ No attendance recorded for today yet.")
