# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

# Warm-up: Three bugs fixed
marks = [90, 25, 70]
passing = []
for mark in marks:                 # Bug 1: iterate over every mark, not len(marks)-1.
    if mark >= 33:                  # Bug 2: append each passing mark; do not replace the list.
        passing.append(mark)
print(sum(passing) / len(passing))  # Bug 3: divide by passing count, not total mark count.

# Build: Grade function with validation (tested in test_grades.py)
def grade(marks: float) -> str:
    if not 0 <= marks <= 100:
        raise ValueError("Marks must be between 0 and 100.")
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B"
    if marks >= 60:
        return "C"
    if marks >= 33:
        return "D"
    return "Fail"

if __name__ == "__main__":
    print("Grade for 80:", grade(80))
    print("Run tests with: pytest -v")
