import csv
import os
from project import calculate_average, get_letter_grade, load_students


def test_calculate_average():
    assert calculate_average("100,90,80") == 90
    assert calculate_average("50,50") == 50
    assert calculate_average("75") == 75
    assert calculate_average("") is None


def test_get_letter_grade():
    assert get_letter_grade(95) == "A"
    assert get_letter_grade(85) == "B"
    assert get_letter_grade(75) == "C"
    assert get_letter_grade(65) == "D"
    assert get_letter_grade(55) == "F"
    assert get_letter_grade(None) == "N/A"


def test_load_students():
    with open("students.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "grades"])
        writer.writeheader()
        writer.writerow({"name": "John", "grades": "90,80"})
        writer.writerow({"name": "Alice", "grades": "100"})

    students = load_students()

    assert len(students) == 2
    assert students[0]["name"] == "John"
    assert students[0]["grades"] == "90,80"
    assert students[1]["name"] == "Alice"
    assert students[1]["grades"] == "100"

    os.remove("students.csv")
