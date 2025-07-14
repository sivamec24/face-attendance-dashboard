from sklearn.neighbors import KNeighborsClassifier
import cv2
import pickle
import numpy as np
import os
import csv
import time
import pyttsx3
from datetime import datetime

# ✅ Base directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
ATTENDANCE_DIR = os.path.join(BASE_DIR, "Attendance")

# ✅ Speak welcome message
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

speak("Welcome")

# ✅ Ensure folders exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(ATTENDANCE_DIR, exist_ok=True)

# ✅ Load face data and labels
with open(os.path.join(DATA_DIR, 'names.pkl'), 'rb') as w:
    LABELS = pickle.load(w)
with open(os.path.join(DATA_DIR, 'faces_data.pkl'), 'rb') as f:
    FACES = pickle.load(f)

print('Shape of Faces matrix -->', FACES.shape)

# ✅ Train KNN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)

# ✅ Initialize webcam
video = cv2.VideoCapture(0)

# ✅ Load Haar cascade
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# ✅ Attendance columns
COL_NAMES = ['NAME', 'TIME']

while True:
    ret, frame = video.read()
    if not ret:
        print("[ERROR] Failed to capture video frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        crop_img = frame[y:y + h, x:x + w]
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)
        output = knn.predict(resized_img)

        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        attendance = [str(output[0]), str(timestamp)]
        attendance_file = os.path.join(ATTENDANCE_DIR, f"Attendance_{date}.csv")
        exist = os.path.isfile(attendance_file)

        # Draw rectangle and label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), (50, 50, 255), -1)
        cv2.putText(frame, str(output[0]), (x + 5, y - 15), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)

    # ✅ Show instructions on the webcam frame
    instruction_text = "Press 'o' for attendance | Press 'q' to quit"
    cv2.putText(frame, instruction_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.imshow("Face Recognition Login System", frame)

    k = cv2.waitKey(1)
    if k == ord('o'):
        speak("Attendance Taken.")
        with open(attendance_file, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if not exist:
                writer.writerow(COL_NAMES)
            writer.writerow(attendance)
        time.sleep(1)

    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
