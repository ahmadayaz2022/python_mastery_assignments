# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from datetime import date
from pathlib import Path
import math
import random
import statistics

# Warm-up: Standard library tour
students = ["Ali", "Sara", "Usman", "Ayesha", "Hamza"]
marks = [75, 82, 90, 68, 85]
today = date.today()
year_end = date(today.year, 12, 31)
print("Square root of 144:", math.sqrt(144))
print("Random student:", random.choice(students))
print("Days until 31 December:", (year_end - today).days)
print("Mean marks:", statistics.mean(marks))
print("Median marks:", statistics.median(marks))

# Build: Own module demonstration.
# The complete reusable module and main.py are in the school_tools_demo folder.
print("See school_tools_demo/school_tools.py and school_tools_demo/main.py.")
