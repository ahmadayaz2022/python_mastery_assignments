# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from typing import Iterable

# Warm-up: Small helpers
def area_of_circle(radius: float) -> float:
    """Return the area of a circle."""
    return 3.141592653589793 * radius ** 2

def is_even(number: int) -> bool:
    """Return True if number is even."""
    return number % 2 == 0

def greet(name: str, lang: str = "en") -> str:
    """Return a greeting in English or Urdu-style Roman script."""
    if lang == "ur":
        return f"Salaam, {name}!"
    return f"Hello, {name}!"

for radius in (2, 3, 4):
    print(f"Circle area ({radius}): {area_of_circle(radius):.2f}")
for number in (4, 7, 10):
    print(f"{number} is even: {is_even(number)}")
for person, language in (("Ali", "en"), ("Sara", "ur"), ("Ahmad", "en")):
    print(greet(person, language))

# Build: Marks toolkit
def average(marks: Iterable[float]) -> float:
    values = list(marks)
    if not values:
        raise ValueError("Marks cannot be empty.")
    return sum(values) / len(values)

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

def report(name: str, marks: list[float]) -> str:
    avg = average(marks)
    return f"{name}: average={avg:.2f}, grade={grade(avg)}"

students = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Usman": [35, 68, 74],
}
for student_name, student_marks in students.items():
    print(report(student_name, student_marks))

# Challenge: Comprehensions
numbers_squared = [number ** 2 for number in range(1, 11)]
long_names = [name for name in ["Ali", "Ahmad", "Usman", "Sara", "Ayesha"] if len(name) > 4]
averages = {name: average(marks) for name, marks in students.items()}
passing_students = [name for name, avg in averages.items() if avg >= 33]
print(numbers_squared)
print(long_names)
print(averages)
print(passing_students)
