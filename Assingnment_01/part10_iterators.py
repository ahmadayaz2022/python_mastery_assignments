# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from functools import wraps
from pathlib import Path
from time import perf_counter

# Warm-up: Countdown and even-number generators
def countdown(number: int):
    while number >= 0:
        yield number
        number -= 1

def evens(limit: int):
    for number in range(0, limit + 1, 2):
        yield number

print("Countdown:", list(countdown(5)))
print("Evens:", list(evens(10)))

# Build: Generate a sample log, then read it lazily
log_path = Path("sample_log.txt")
with log_path.open("w", encoding="utf-8") as log_file:
    for line_number in range(1, 61):
        word = "ERROR" if line_number % 7 == 0 else "INFO"
        log_file.write(f"{word}: Log message number {line_number}\n")

def read_lines(path: str):
    with open(path, encoding="utf-8") as source:
        for line in source:
            yield line.rstrip("\n")

def only_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

for error_line in only_errors(read_lines(str(log_path))):
    print(error_line)

# Challenge: Decorators
def timer(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = function(*args, **kwargs)
        print(f"{function.__name__} took {perf_counter() - start:.6f} seconds")
        return result
    return wrapper

def log_calls(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"Calling {function.__name__} args={args}, kwargs={kwargs}")
        return function(*args, **kwargs)
    return wrapper

@timer
@log_calls
def sum_to_million() -> int:
    return sum(range(1, 1_000_001))

print("Sum:", sum_to_million())
