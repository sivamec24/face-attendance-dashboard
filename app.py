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
    page_icon="📋"
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
        background-color: rgba(255, 255, 255, 0.92);
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

# ✅ Title and last updated time
st.title("📋 Face Recognition Attendance Dashboard")
st.caption(f"🕒 Last updated: `{timestamp}`")

# ✅ Auto-refresh every 2 seconds
st_autorefresh(interval=2000, limit=None, key="autorefresh")

# ✅ Path to today's attendance file
attendance_file = f"Attendance/Attendance_{date}.csv"

# ✅ Display the attendance DataFrame
if os.path.exists(attendance_file):
    try:
        df = pd.read_csv(attendance_file)
        if not df.empty and 'NAME' in df.columns and 'TIME' in df.columns:
            df = df[['NAME', 'TIME']]  # Display only relevant columns
            st.subheader("✅ Attendance Records")
            st.dataframe(df, use_container_width=True)

            # Optional summary
            st.markdown("### 📈 Summary")
            st.write(f"🧍 Total Entries Today: **{len(df)}**")
            st.write(f"👤 Unique People: **{df['NAME'].nunique()}**")

        else:
            st.warning("⚠️ Attendance file is empty or malformed.")
    except Exception as e:
        st.error(f"❌ Error loading CSV: `{e}`")
else:
    st.info("📭 No attendance file found for today yet.")
