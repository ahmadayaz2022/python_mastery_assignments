# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from typing import Sequence

def average(marks: Sequence[float]) -> float:
    if not marks:
        raise ValueError("Marks cannot be empty.")
    return sum(marks) / len(marks)

def grade(avg: float) -> str:
    if not 0 <= avg <= 100:
        raise ValueError("Average must be between 0 and 100.")
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 33:
        return "D"
    return "Fail"

def report(name: str, marks: Sequence[float]) -> str:
    avg = average(marks)
    return f"{name}: average={avg:.2f}, grade={grade(avg)}"

if __name__ == "__main__":
    print(report("Ali", [80, 75, 90]))
