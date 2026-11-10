# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

from collections.abc import Iterable

def attendance_percentage(present_days: int, total_days: int) -> float:
    if total_days <= 0:
        raise ValueError("Total days must be greater than zero.")
    if not 0 <= present_days <= total_days:
        raise ValueError("Present days must be between zero and total days.")
    return present_days / total_days * 100

def validate_roll_number(roll_number: int, existing_roll_numbers: Iterable[int]) -> bool:
    return roll_number > 0 and roll_number not in existing_roll_numbers
