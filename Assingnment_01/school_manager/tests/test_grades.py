# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

import pytest
from school.grades import calculate_grade
from school.models import Student
from school.comments import make_comment
from school.attendance import attendance_percentage

@pytest.mark.parametrize(
    ("marks", "expected"),
    [
        (0, "Fail"),
        (32, "Fail"),
        (33, "D"),
        (59, "D"),
        (60, "C"),
        (69, "C"),
        (70, "B"),
        (79, "B"),
        (80, "A"),
        (100, "A"),
    ],
)
def test_grade_boundaries(marks: float, expected: str) -> None:
    assert calculate_grade(marks) == expected

def test_grade_rejects_out_of_range_marks() -> None:
    with pytest.raises(ValueError):
        calculate_grade(101)

def test_student_average_and_report() -> None:
    student = Student("Ali", 12, [80, 70, 90])
    assert student.average == 80
    assert "Grade: A" in student.report()

def test_student_rejects_invalid_mark() -> None:
    student = Student("Sara", 13)
    with pytest.raises(ValueError):
        student.add_mark(120)

def test_teacher_comment_for_high_performance() -> None:
    assert make_comment(Student("Ayesha", 14, [90, 85])) == "Excellent in all subjects, keep it up."

def test_attendance_percentage() -> None:
    assert attendance_percentage(18, 20) == 90

def test_attendance_rejects_invalid_total() -> None:
    with pytest.raises(ValueError):
        attendance_percentage(2, 0)
