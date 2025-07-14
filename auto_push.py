import subprocess
from datetime import datetime

# ✅ Auto commit and push attendance changes
message = f"📌 Auto-update attendance: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

try:
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", message], check=True)
    subprocess.run(["git", "push"], check=True)
    print("✅ Successfully pushed to GitHub.")
except subprocess.CalledProcessError as e:
    print(f"❌ Git push failed: {e}")
