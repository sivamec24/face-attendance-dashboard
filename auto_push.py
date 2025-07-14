import subprocess
from datetime import datetime

# 📝 Git commit message with timestamp
commit_message = f"Auto-update attendance: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Run git commands
subprocess.run(["git", "add", "Attendance/"])
subprocess.run(["git", "commit", "-m", commit_message])
subprocess.run(["git", "push"])
