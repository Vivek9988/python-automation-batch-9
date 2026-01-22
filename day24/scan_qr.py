# scan_qr.py

import cv2
import csv
import time
from datetime import datetime
from team_data import team_members

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

attendance_file = "attendance_log.csv"

# Create CSV file with header if not exists
try:
    with open(attendance_file, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "ID", "Name", "Role"])
except FileExistsError:
    pass

print("📷 Show QR to camera (auto stop in 15 seconds)")

start_time = time.time()
MAX_TIME = 15

while True:
    if time.time() - start_time > MAX_TIME:
        print("⏹️ Time limit reached. Scanner stopped.")
        break

    ret, frame = cap.read()
    if not ret:
        print("❌ Camera error")
        break

    data, _, _ = detector.detectAndDecode(frame)

    cv2.imshow("QR Scanner", frame)

    if data:
        if data in team_members:
            member = team_members[data]
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print("\n✅ VALID QR")
            print("Name:", member["name"])
            print("Role:", member["role"])
            print("ID:", data)
            print("Time:", timestamp)

            with open(attendance_file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([timestamp, data, member["name"], member["role"]])

            print("📝 Attendance saved!")
            break
        else:
            print("❌ Invalid QR")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
