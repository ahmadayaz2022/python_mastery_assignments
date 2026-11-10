# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from datetime import date
from pathlib import Path
import csv
import json

# Warm-up: Safe division
while True:
    try:
        numerator = float(input("Numerator: "))
        denominator = float(input("Denominator: "))
        print("Result:", numerator / denominator)
        break
    except ValueError:
        print("Please enter numbers only.")
    except ZeroDivisionError:
        print("The denominator cannot be zero.")

# Build: Daily diary
diary_path = Path("diary.txt")
while True:
    print("\n1) Add note  2) Read entries  3) Exit")
    choice = input("Choose: ").strip()
    if choice == "1":
        note = input("Write today's note: ").strip()
        with diary_path.open("a", encoding="utf-8") as diary:
            diary.write(f"{date.today().isoformat()}: {note}\n")
        print("Note saved.")
    elif choice == "2":
        if diary_path.exists():
            print(diary_path.read_text(encoding="utf-8"))
        else:
            print("No entries yet")
    elif choice == "3":
        break
    else:
        print("Invalid choice.")

# Challenge: Save sample class results to CSV and JSON
results = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Usman": [35, 68, 74],
    "Ayesha": [82, 39, 91],
    "Hamza": [65, 70, 78],
}
with open("results.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["name", "mark1", "mark2", "mark3", "average"])
    for name, marks in results.items():
        writer.writerow([name, *marks, round(sum(marks) / len(marks), 2)])

json_data = [
    {"name": name, "marks": marks, "average": round(sum(marks) / len(marks), 2)}
    for name, marks in results.items()
]
with open("results.json", "w", encoding="utf-8") as json_file:
    json.dump(json_data, json_file, indent=4)

with open("results.csv", newline="", encoding="utf-8") as csv_file:
    rows = list(csv.DictReader(csv_file))
topper = max(rows, key=lambda row: float(row["average"]))
print(f"CSV topper: {topper['name']} ({topper['average']})")
