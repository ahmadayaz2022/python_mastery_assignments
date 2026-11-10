# Name: Ahmad Ayaz
# Trainee ID: TRN-2026-000371
# Date: 09 November 2026

import json
import logging
from dataclasses import asdict
from pathlib import Path
from .models import Student

LOGGER = logging.getLogger(__name__)
DATA_FILE = Path(__file__).resolve().parent.parent / "school.json"

def load_students(path: Path = DATA_FILE) -> list[Student]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return [Student(**item) for item in data]
    except (json.JSONDecodeError, TypeError, ValueError) as error:
        LOGGER.exception("Could not load student data: %s", error)
        raise ValueError("The school data file is invalid.") from error

def save_students(students: list[Student], path: Path = DATA_FILE) -> None:
    data = [asdict(student) for student in students]
    path.write_text(json.dumps(data, indent=4), encoding="utf-8")
    LOGGER.info("Saved %d students to %s", len(students), path)
