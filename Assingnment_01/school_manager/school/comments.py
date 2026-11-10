# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from .models import Student

def make_comment(student: Student) -> str:
    """Create a simple teacher comment using transparent mark-based rules."""
    if not student.marks:
        return "Marks have not been added yet."
    if all(mark >= 80 for mark in student.marks):
        return "Excellent in all subjects, keep it up."
    if student.average >= 80:
        return "Excellent overall performance. Keep working consistently."
    if student.average >= 60:
        return "Good effort. Focus on the subjects with lower marks."
    if student.average >= 33:
        return "You are making progress. More regular practice will help."
    return "Please seek support and make a focused plan to improve."
