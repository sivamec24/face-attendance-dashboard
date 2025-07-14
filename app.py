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
    body {
        background-image: url('https://images.unsplash.com/photo-1521791136064-7986c2920216?fit=crop&w=1400&q=80');
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }
    .stApp {
        background-color: rgba(255, 255, 255, 0.88);
        padding: 2rem;
        border-radius: 12px;
    }
    h1, h2, h3, h4 {
        color: #1c2c4c;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Current date and time
ts = time.time()
date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")

# ✅ Title and update time
st.title("📋 Face Recognition Attendance Dashboard")
st.markdown(f"🕒 **Last updated:** `{timestamp}`")

# ✅ Auto-refresh every 2 seconds
st_autorefresh(interval=2000, limit=None, key="autorefresh")

# ✅ Attendance file path
attendance_file = f"Attendance/Attendance_{date}.csv"

# ✅ Display data
if os.path.exists(attendance_file):
    try:
        df = pd.read_csv(attendance_file)
        df = df[['NAME', 'TIME']]  # only show required columns
        st.subheader("✅ Attendance Records")
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"⚠️ Failed to load CSV: {e}")
else:
    st.warning("⚠️ No attendance recorded for today yet.")
