# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from collections.abc import Sequence

def calculate_average(marks: Sequence[float]) -> float:
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

def calculate_grade(average: float) -> str:
    if not 0 <= average <= 100:
        raise ValueError("Average must be between 0 and 100.")
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 33:
        return "D"
    return "Fail"
