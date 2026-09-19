# Python Console Attendance Tracking System

A lightweight, terminal-based attendance management system built entirely with Python's standard library. The tool records attendance entries, logs accurate date and time stamps, prevents duplicate daily check-ins, and persists data directly into a structured CSV file without external dependencies.

---

## 📌 Features

* **Zero External Dependencies:** Built strictly using Python built-ins (`csv`, `datetime`, and `os`).
* **Automated Timestamps:** Logs separate `date` (`YYYY-MM-DD`) and `time` (`HH:MM:SS`) columns automatically using `datetime.now()`.
* **Duplicate Entry Guard:** Cross-checks the student ID against existing entries for the current date to prevent multiple check-ins on the same day.
* **Persistent CSV Storage:** Automatically creates `attendance.csv` and initializes headers if missing, appending subsequent records using safe append mode (`'a'`).
* **Continuous Check-in Loop:** Runs continuously for multiple students and supports a graceful sentinel shutdown via typing `exit`.

---

## 📊 CSV Data Schema

Each entry is appended to `attendance.csv` with the following columns:

| Index | Field | Description | Example |
| :--- | :--- | :--- | :--- |
| `0` | `studentID` | Unique student identifier | `S101` |
| `1` | `name` | Student's full name | `Jane Doe` |
| `2` | `subject` | Academic course or subject | `Computer Science` |
| `3` | `facultyID` | Instructor's ID | `F-402` |
| `4` | `facultyName` | Instructor's name | `Dr. Alan Turing` |
| `5` | `status` | Attendance status | `Present` or `Absent` |
| `6` | `date` | Check-in date (`YYYY-MM-DD`) | `2026-09-19` |
| `7` | `time` | Check-in time (`HH:MM:SS`) | `14:35:10` |

---

## 🛠️ Requirements

* **Python 3.7+** installed on your system.
* No additional packages or virtual environments are required.

---

## 🚀 Getting Started

### 1. Clone or Download the Repository

```bash
git clone https://github.com/your-username/python-attendance-system.git
cd python-attendance-system
```

### 2. Run the Script

Launch the program from your terminal or command prompt:

```bash
python attendance.py
```

---

## 💻 Example Usage

```text
--- Attendance System Started ---

Enter Student ID (or type 'exit' to stop): S101
Enter Student Name: Jane Doe
Enter Subject: Data Structures
Enter Faculty ID: F-12
Enter Faculty Name: Prof. Smith
Enter Status (Present/Absent): Present
✅ Attendance marked successfully!

Enter Student ID (or type 'exit' to stop): S101
Enter Student Name: Jane Doe
Enter Subject: Data Structures
Enter Faculty ID: F-12
Enter Faculty Name: Prof. Smith
Enter Status (Present/Absent): Present
⚠️ Attendance already marked for today! Please come back tomorrow.

Enter Student ID (or type 'exit' to stop): exit
System closed successfully.
```

---

## 📂 File Structure

```text
.
├── attendance.py       # Main Python script
├── attendance.csv      # Auto-generated CSV file storing entries
└── README.md           # Documentation
```

---

## 🗺️ Roadmap & Future Enhancements

- [ ] **Input Sanitization:** Add strict choices for `status` (`Present` / `Absent`).
- [ ] **Reporting Engine:** Generate summary metrics (e.g., student attendance percentage by subject).
- [ ] **Graphical Interface:** Rebuild the terminal prompts into a desktop UI using Python's `tkinter`.
- [ ] **Relational Database:** Migrate storage from CSV to an `sqlite3` database for complex querying.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
