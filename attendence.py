import csv
import os
from datetime import datetime

FILE_NAME = "attendance.csv"

print("--- Attendance System Started ---")

while True:
    # 1. Prompt for Student ID or Exit
    student_id = input("\nEnter Student ID (or type 'exit' to stop): ").strip()
    if student_id.lower() == "exit":
        print("System closed successfully.")
        break

    # 2. Collect remaining details
    name = input("Enter Student Name: ").strip()
    subject = input("Enter Subject: ").strip()
    faculty_id = input("Enter Faculty ID: ").strip()
    faculty_name = input("Enter Faculty Name: ").strip()
    status = input("Enter Status (Present/Absent): ").strip()

    # 3. Capture current timestamp
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M:%S")

    # 4. Check for duplicate entry today
    already_marked = False
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == student_id and row[6] == current_date:
                    already_marked = True
                    break

    # 5. Save or report duplicate
    if already_marked:
        print("⚠️ Attendance already marked for today! Please come back tomorrow.")
    else:
        file_exists = os.path.exists(FILE_NAME)
        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file)

            # Write header row on initial file creation
            if not file_exists:
                writer.writerow(
                    [
                        "studentID",
                        "name",
                        "subject",
                        "facultyID",
                        "facultyName",
                        "status",
                        "date",
                        "time",
                    ]
                )

            writer.writerow(
                [
                    student_id,
                    name,
                    subject,
                    faculty_id,
                    faculty_name,
                    status,
                    current_date,
                    current_time,
                ]
            )

        print("✅ Attendance marked successfully!")
