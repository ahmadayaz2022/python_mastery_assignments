# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from dataclasses import dataclass, field
from .grades import calculate_average, calculate_grade

@dataclass
class Student:
    name: str
    roll_number: int
    marks: list[float] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Student name cannot be empty.")
        if self.roll_number <= 0:
            raise ValueError("Roll number must be positive.")
        if any(mark < 0 or mark > 100 for mark in self.marks):
            raise ValueError("Every mark must be between 0 and 100.")

    @property
    def average(self) -> float:
        return calculate_average(self.marks)

    @property
    def grade(self) -> str:
        return calculate_grade(self.average)

    def add_mark(self, mark: float) -> None:
        if not 0 <= mark <= 100:
            raise ValueError("Mark must be between 0 and 100.")
        self.marks.append(mark)

    def report(self) -> str:
        marks_text = ", ".join(f"{mark:g}" for mark in self.marks) or "No marks"
        return (
            f"Name: {self.name} | Roll: {self.roll_number} | "
            f"Marks: {marks_text} | Average: {self.average:.2f} | Grade: {self.grade}"
        )
