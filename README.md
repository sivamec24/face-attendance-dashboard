🎯 Face Recognition Attendance System
An AI-powered real-time face recognition attendance system using OpenCV, KNN, and Streamlit.
It allows you to capture attendance using your webcam and visualize it through a modern dashboard.

📂 Project Structure
graphql
Copy
Edit
face-attendance-system/
├── test.py                     # Local face recognition & attendance capture
├── dashboard.py                # Streamlit dashboard to display attendance
├── data/                       # Stores face data (names.pkl, faces_data.pkl)
├── Attendance/                 # Daily CSV files (e.g., Attendance_14-07-2025.csv)
├── requirements.txt            # Dependencies for dashboard
├── README.md                   # Project documentation
💡 Features
✅ Real-time face recognition
✅ Automatically records timestamped attendance
✅ Saves data as daily CSV files
✅ Streamlit dashboard with auto-refresh and styled display
✅ Works offline for attendance capture

🧠 Technologies Used
Python 3.10+

OpenCV – Face detection

KNeighborsClassifier – Face recognition

pyttsx3 – Text-to-speech

pandas – Data handling

Streamlit – Dashboard

streamlit-autorefresh – Live updates

⚙️ How It Works
👤 Face Capture & Recognition (Run Locally)
Run test.py to:

Detect and recognize faces via webcam

Save attendance with current time to Attendance/Attendance_<date>.csv

bash
Copy
Edit
python test.py
📊 Streamlit Dashboard (Deployed or Local)
Run dashboard.py to:

View daily attendance CSV

Auto-refresh every 2 seconds

Styled display of Name and Time

bash
Copy
Edit
streamlit run dashboard.py
🚀 Deployment (Streamlit Cloud)
1. Add requirements.txt
txt
Copy
Edit
streamlit
pandas
streamlit-autorefresh
2. Push to GitHub
bash
Copy
Edit
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/face-attendance-system.git
git push -u origin main
3. Deploy
Go to: https://streamlit.io/cloud

Connect your GitHub repo

Select dashboard.py as the app file

📦 Future Improvements
Upload CSVs to Google Sheets or Firebase

Admin login for dashboard

Email or SMS alerts

Multiple camera support

🧑‍💻 Author
Siva 
Project built for educational purposes and real-world automation using AI and Python.

🛡 License
This project is open-source under the MIT License