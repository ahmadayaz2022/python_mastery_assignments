# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

import logging
from school.comments import make_comment
from school.models import Student
from school.storage import load_students, save_students

logging.basicConfig(
    filename="school_manager.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
LOGGER = logging.getLogger(__name__)

def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a numeric value.")

def find_student(students: list[Student], roll_number: int) -> Student | None:
    for student in students:
        if student.roll_number == roll_number:
            return student
    return None

def add_student(students: list[Student]) -> None:
    name = input("Student name: ").strip()
    roll_number = read_int("Roll number: ")
    if find_student(students, roll_number):
        print("That roll number already exists.")
        return
    try:
        students.append(Student(name=name, roll_number=roll_number))
        print("Student added.")
        LOGGER.info("Added student roll=%s", roll_number)
    except ValueError as error:
        print(f"Could not add student: {error}")

def add_marks(students: list[Student]) -> None:
    roll_number = read_int("Student roll number: ")
    student = find_student(students, roll_number)
    if student is None:
        print("Student not found.")
        return
    mark = read_float("Mark (0-100): ")
    try:
        student.add_mark(mark)
        print("Mark added.")
        LOGGER.info("Added mark for roll=%s", roll_number)
    except ValueError as error:
        print(error)

def show_report(students: list[Student]) -> None:
    roll_number = read_int("Student roll number: ")
    student = find_student(students, roll_number)
    if student is None:
        print("Student not found.")
    else:
        print("\nREPORT CARD")
        print(student.report())
        print("Teacher comment:", make_comment(student))

def show_ranking(students: list[Student]) -> None:
    ranked = sorted(students, key=lambda student: student.average, reverse=True)
    if not ranked:
        print("No students have been added.")
        return
    print("\nCLASS RANKING")
    for position, student in enumerate(ranked, start=1):
        print(f"{position}. {student.name} (Roll {student.roll_number}) - {student.average:.2f} ({student.grade})")

def write_comment(students: list[Student]) -> None:
    roll_number = read_int("Student roll number: ")
    student = find_student(students, roll_number)
    if student is None:
        print("Student not found.")
    else:
        print(make_comment(student))

def run() -> None:
    students = load_students()
    while True:
        print("\n===== SCHOOL MANAGER =====")
        print("1. Add student")
        print("2. Add marks")
        print("3. Show report card")
        print("4. Class ranking")
        print("5. Write comment")
        print("6. Save and exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                add_marks(students)
            elif choice == "3":
                show_report(students)
            elif choice == "4":
                show_ranking(students)
            elif choice == "5":
                write_comment(students)
            elif choice == "6":
                save_students(students)
                print("Data saved. Goodbye!")
                break
            else:
                print("Please choose an option from 1 to 6.")
        except (OSError, ValueError) as error:
            LOGGER.exception("Operation failed")
            print(f"Operation failed: {error}")

if __name__ == "__main__":
    run()
